from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt


class NeighbourhoodTest(TestCase):
    def setUp(self):
        self.Hood = Neighbourhood(name='Hood', location="Nairobi", occupants=1, admin=User(id=1))

    def test_instance(self):
        self.assertTrue(isinstance(self.Hood,Neighbourhood))

    def tearDown(self):
        Neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Hood.save_neighbourhood()
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Hood.delete_neighbourhood('Hood')
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

class HealthTestClass(TestCase):
    def setUp(self):
        self.Hood = Neighbourhood(name='Hood', location="Nairobi", occupants=1, admin=User(id=1))
        self.Hood.save_neighbourhood()
        self.Matter = Health(logo="hood.png", neighbourhood=self.Hood, name='Matter', email="test@gmail.com", contact=712345678)

    def test_instance(self):
        self.assertTrue(isinstance(self.Matter,Health))

    def tearDown(self):
        Health.objects.all().delete()

    def test_save_method(self):
        self.Matter.save_health()
        health = Health.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Matter.delete_health('Matter')
        health = Health.objects.all()
        self.assertTrue(len(health)==0)
    

class TestProfile(TestCase):
    def setUp(self):
        self.Hood = Neighbourhood(name='Hood', location="Nairobi", occupants=1, admin=User(id=1))
        self.profile=Profile(user=User(id=1),profilepic="img.png",bio="Funlife",neighbourhood=self.Hood, profile_email="test@gmail.com")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_initialization(self):
        self.assertEqual(self.profile.profilepic,"img.png")
        self.assertEqual(self.profile.bio,"Funlife")

    def test_save(self):
        self.Hood.save_neighbourhood()
        self.profile.save_profile()
        prof=Profile.objects.all()
        self.assertTrue(len(prof)>0)

    def test_delete(self):
        self.profile.delete_profile('profile')
        prof=Profile.objects.all()
        self.assertEqual(len(prof),0)



