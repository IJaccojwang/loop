from django import forms
from .models import Notifications,Business,Profile

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['user','neighbourhood_id']

class NotificationForm(forms.ModelForm):
    class Meta:
        model=Notifications
        exclude=['author','neighbourhood','post_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']