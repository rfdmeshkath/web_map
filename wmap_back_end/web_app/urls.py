from django.contrib import admin
from django.urls import include, path
from . import views
from .views import LoginView, LogoutView


# defining my url patterns here
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/web_app/auth/login/', LoginView.as_view()),
    path('api/v1/web_app/auth/logout/', LogoutView.as_view()),

    path('api/v1/web_app/users/', views.ListUsers.as_view()),
    path('api/v1/web_app/users/<int:pk>/', views.DetailUsers.as_view()),

    path('api/v1/get_all_stations/', views.get_all_stations),
    path('api/v1/get_stations_near_to_me/', views.get_nearer_stations),
    path('api/v1/get_stations_near_to_a_location/', views.get_stations_near_to_a_location),

]
