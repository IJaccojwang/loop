from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *

@login_required(login_url='/accounts/login/')
def index(request):
    try:
        current_user=request.user
        profile =Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('edit')
    
    return render(request,'index.html')

def profile(request):
    current_user=request.user
    profile =Profile.objects.get(user=current_user)

    return render(request,'profile.html',{"profile":profile})

def edit_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:

        form = ProfileForm()
    return render(request,'edit_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def health(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    health= Health.objects.filter(neighbourhood=profile.neighbourhood_id)

    return render(request,'health.html',{"health":health})

@login_required(login_url='/accounts/login/')
def news(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    notifications = Notifications.objects.filter(neighbourhood=profile.neighbourhood_id)

    return render(request,'notifications.html',{"notifications":all_notifications})


@login_required(login_url='/accounts/login/')
def authorities(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    authorities = Authorities.objects.filter(neighbourhood=profile.neighbourhood_id)

    return render(request,'authorities.html',{"authorities":authorities})

@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user=request.user
    profile=Profile.objects.get(user=current_user)
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood_id)

    return render(request,'businesses.html',{"businesses":businesses})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user=request.user
    profile =Profile.objects.get(user=current_user)

    if request.method=="POST":
        form =BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.owner = current_user
            business.neighbourhood = profile.neighbourhood_id
            business.save()

        return HttpResponseRedirect('/businesses')

    else:
        form = BusinessForm()

    return render(request,'business_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_notification(request):
    current_user=request.user
    profile =Profile.objects.get(user=current_user)

    if request.method=="POST":
        form = NotificationForm(request.POST,request.FILES)
        if form.is_valid():
            notification = form.save(commit = False)
            notification.author = current_user
            notification.neighbourhood = profile.neighbourhood_id
            notification.save()

        return HttpResponseRedirect('/notifications')


    else:
        form = NotificationForm()

    return render(request,'notifications_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(user=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('index')

    elif Profile.objects.get(user=current_user):
        profile = Profile.objects.get(user=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'update_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_bussinesses = Business.search_business(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"businesses":searched_bussinesses})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})