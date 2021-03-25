from django.db import models

class dataStore(models.Model):
    name = models.CharField(max_length=50, default="Your name please")
    age = models.IntegerField()

##model for storing the user details
class userDetail(models.Model):
    firstname = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    date = models.IntegerField()
    month = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)

