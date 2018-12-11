from django.db import models


class User(models.Model):
    # defining database table
    username = models.CharField(max_length=50)
    monitoring_station = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    monitoring_time = models.TimeField(blank=True)

    def __str__(self):
        """A string representation of the model."""
        return self.username