from django.db import models
from django.contrib.auth.models import User



class Neighbourhood(models.Model):
    '''
    Model for each neighbourhood instatnce
    '''
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(name=neighbourhood).delete()

    @classmethod
    def update_neighbourhood(cls,neighbourhood, new_neighbourhood):
        cls.objects.filter(name=neighbourhood).update(name=new_neighbourhood)
    
    @classmethod
    def update_occupants(cls,neighbourhood, new_occupants):
        cls.objects.filter(name=neighbourhood).update(occupants=new_occupants)
    
    @classmethod
    def find_neighbourhood(cls,term):
        result=cls.objects.filter(name__icontains=term)
        return result


class Profile(models.Model):
    '''
    Model for each profile instatnce
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=255)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    profile_email = models.CharField(max_length=255)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()
    
    @classmethod
    def delete_profile(cls,username):
        cls.objects.filter(user=username).delete()
    

class Business(models.Model):
    '''
    Model for each business instatnce
    '''
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    neighbourhood_id = models.ForeignKey(Neighbourhood)
    business_email = models.CharField(max_length=100)

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    @classmethod
    def delete_business(cls,business):
        cls.objects.filter(business_name=business).delete()
    
    @classmethod
    def update_business(cls,business, new_email):
        cls.objects.filter(business_name=business).update(business_email=new_email)

    @classmethod
    def find_business(cls,term):
        result=cls.objects.filter(business_name__icontains=term)
        return result


class Notifications(models.Model):
    '''
    Model for each notification instatnce
    '''
    title = models.CharField(max_length=100)
    notification = models.CharField(max_length=600)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save_notification(self):
        self.save()
    
    @classmethod
    def delete_notification(cls,title):
        cls.objects.filter(title=title).delete()

class Health(models.Model):
    '''
    Model for each health instatnce
    '''
    logo = models.ImageField(upload_to='healthlogo/')
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name
    
    def save_health(self):
        self.save()
    
    @classmethod
    def delete_health(cls,name):
        cls.objects.filter(name=name).delete()

class Authorities(models.Model):
    '''
    Model for each authority instatnce
    '''
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name
    
    def save_authority(self):
        self.save()
    
    @classmethod
    def delete_authority(cls,name):
        cls.objects.filter(name=name).delete()