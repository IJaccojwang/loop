from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns=[
    url('^$', views.index, name = 'index'),
    url(r'^profile$',views.profile,name='profile'),
    url(r'^profile/edit$',views.edit_profile,name='edit'),
    url(r'^profile/update$',views.update_profile, name='update_profile'),
    url(r'^notifications$',views.news, name='notifications'),
    url(r'^notifications/new$',views.new_notification, name='new_notification'),
    url(r'^health$',views.health, name='health'),
    url(r'^authorities$',views.authorities, name='authorities'),
    url(r'^businesses$',views.businesses, name='businesses'),
    url(r'^businesses/new$',views.new_business, name='new_business'),
    url(r'^search/',views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)