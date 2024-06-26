from django.db import models
from django.contrib.auth.models import User


class PollUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
    
    
class Addinfo(models.Model):
    title = models.CharField('title', max_length = 50)
    anons = models.CharField('anons', max_length = 50)
    date = models.DateTimeField("date")
    
    def __str__(self):
        return self.title
    
