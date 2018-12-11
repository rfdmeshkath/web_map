FROM python:3.5

MAINTAINER Rafid

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get -y install libgdal-dev

RUN mkdir -p /wmap_back

COPY requirements.txt /wmap_back

COPY . /wmap_back

WORKDIR /wmap_back

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

