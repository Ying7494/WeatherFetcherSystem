from django.db import models



class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    class Meta:
        db_table = "User"

class Weather(models.Model):
    city = models.CharField(max_length=20) #City NO
    temp = models.FloatField() #Temperature
    humd = models.FloatField() #Humidity
    pres = models.FloatField() #Pressure
    wdir = models.FloatField() #Wind Direction
    wdsd = models.FloatField() #Wind Speed
    recordTime = models.DateTimeField() #Time
    class Meta:
        db_table = "Weather"

