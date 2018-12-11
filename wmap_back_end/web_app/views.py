from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from django.contrib.auth import login as  django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from web_app import models
from . import serializers
from .serializers import LoginSerializer
from web_app.map_helper import distance_checker, retrieve_coordinates_from_address
from web_app.data_collector import dublin_bike_api


class ListUsers(generics.ListCreateAPIView):
    # lists all user
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    # define who can access this
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
    # gets data of one particular user
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    # define who can access this
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class LoginView(APIView):
    # return a token to user once logged in
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)


class LogoutView(APIView):
    # logout user
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        django_logout(request)
        return Response(status=204)

# setting the walking range in kilometers
walking_range = 1.5


def get_all_stations(request):
    """
    this view function gets all the bike stop locations data from the api and returns to user
    :param request: nothing
    :return: json response of bike station data
    """
    formatted_data = {}
    counter = 0
    all_stations = dublin_bike_api()
    for station in all_stations:
        formatted_data[counter] = station
        counter = counter + 1
    return JsonResponse(formatted_data)


def get_nearer_stations(request):
    """
    this view function searches the available bike stops with in walking range of a user
    :param request: coordinates of user
    :return: json response which has all the bike station data near to the passed coordinates
    """
    user_latitude = request.GET['latitude']
    user_longitude = request.GET['longitude']
    nearer_stations = {}
    counter = 0
    all_stations = dublin_bike_api()
    for station in all_stations:
        # checking the distance between user and each station
        distance = distance_checker(station['latitude'], station['longitude'], user_latitude, user_longitude)
        if distance < walking_range:  # show the details of only stations which are with in "walking_range" radius
            nearer_stations[counter] = station
            nearer_stations[counter]['distance'] = distance
            counter = counter + 1
    return JsonResponse(nearer_stations)


def get_stations_near_to_a_location(request):
    """
    this view function returns all the bike station around a given location
    :param request: string:address
    :return: json response of bike station data
    """
    address = request.GET['address']
    # getting the coordinates from the address by using google maps api
    latitude, longitude = retrieve_coordinates_from_address(address)
    nearer_stations = {}
    counter = 0
    all_stations = dublin_bike_api()
    # formatting output
    for station in all_stations:
        distance = distance_checker(station['latitude'], station['longitude'], latitude, longitude)
        if distance < walking_range:  # show the details of only stations which are with in "walking_range" radius
            nearer_stations[counter] = station
            nearer_stations[counter]['distance'] = distance
            counter = counter + 1
    return JsonResponse(nearer_stations)
