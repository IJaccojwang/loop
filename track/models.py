from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=255)
    neighbourhood_id = models.CharField(max_length=255)
    profile_email = models.CharField(max_length=255)

    def __str__(self):
        return self.prefname

class Neighbourhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.prefname
    
    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(name=name).delete()

class Business(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    neighbourhood_id = models.ForeignKey(Neighbourhood)
    business_email = models.CharField(max_length=100)

    def __str__(self):
        return self.prefname
