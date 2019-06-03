from django.db import models
from django.contrib.auth.models import User



class Neighbourhood(models.Model):
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
        cls.objects.filter(name=name).delete()


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=255)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    profile_email = models.CharField(max_length=255)

    def __str__(self):
        return self.prefname

    def save_profile(self):
        self.save()
    
    # delete_neigborhood()
    # find_neigborhood(neigborhood_id)
    # update_neighborhood()
    # update_occupants()

class Business(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    neighbourhood_id = models.ForeignKey(Neighbourhood)
    business_email = models.CharField(max_length=100)

    def __str__(self):
        return self.prefname

    def save_business(self):
        self.save()

    # create_business()
    # delete_business()
    # find_business(business_id)
    # update_business()


class Notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = models.CharField(max_length=600)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Residence(models.Model):
	'''
	Model that keeps track of what user has joined what neighbourhood
	'''
	user_id = models.OneToOneField(User)
	neighbourhood = models.ForeignKey(Neighbourhood)

	def __str__(self):
		return self.user_id

class Health(models.Model):
    logo = models.ImageField(upload_to='healthlogo/')
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Authorities(models.Model):
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name