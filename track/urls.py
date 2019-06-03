from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns=[
    url('^$', views.index, name = 'index'),
    url(r'^myprofile$',views.profile,name='myprofile'),
    url(r'^profile/edit$',views.edit_profile,name='edit'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)