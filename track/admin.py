from django.contrib import admin
from .models import Profile, Neighbourhood, Business, Notifications, Health, Authorities

admin.site.register(Profile)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Notifications)
admin.site.register(Health)
admin.site.register(Authorities)

