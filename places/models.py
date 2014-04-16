from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=50)	
    geolocation = models.CharField(max_length=100)

class State(models.Model):
    name = models.CharField(max_length=500)
    country = models.ForeignKey(Country)
    description = models.CharField(max_length=50)	
    geolocation = models.CharField(max_length=100)

class District(models.Model):
    name = models.CharField(max_length=500)
    state = models.ForeignKey(State)
    country = models.ForeignKey(Country)
    description = models.CharField(max_length=50)	
    geolocation = models.CharField(max_length=100)
    

class City(models.Model):
    name = models.CharField(max_length=500)
    district = models.ForeignKey(District)
    state = models.ForeignKey(State)
    country = models.ForeignKey(Country)
    description = models.CharField(max_length=50)	
    geolocation = models.CharField(max_length=100)

class Location(models.Model):
    address = models.CharField(max_length=500)
    city = models.ForeignKey(City)
    district = models.ForeignKey(District)
    state = models.ForeignKey(State)
    country = models.ForeignKey(Country)
    description = models.CharField(max_length=50)	
    geolocation = models.CharField(max_length=100)



