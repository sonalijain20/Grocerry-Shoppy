from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views 'here.

def home(request):
        kitcat = KitchenCategory.objects.all()
        return render(request, "index.html", {"Kitchen": kitcat})


def signupUser(request):
    choice = request.POST.get('option')
    if (choice == 'seller'):
        s = Seller()
        s.name = request.POST.get('name')
        s.uname = request.POST.get('username')
        s.email = request.POST.get('email')
        pword = request.POST.get('password')
        try:
            user = User.objects.create_user(
                username=s.uname, email=s.email, password=pword)
            s.save()
            return HttpResponseRedirect('/')
        except:
            messages.error(request, "Username already exists")
            return render(request, "index.html")
    else:
        b = Buyer()
        b.name = request.POST.get('name')
        # #b.lname=request.POST.get('lname')
        b.uname = request.POST.get('username')
        b.email = request.POST.get('email')
        pword = request.POST.get('password')
        try:
            user = User.objects.create_user(
                username=b.uname, email=b.email, password=pword)
            b.save()
            return HttpResponseRedirect('/')
        except:
            messages.error(request, "Username already exists")
            return render(request, "index.html")
    # b=Buyer()
    # b.name=request.POST.get('name')
    # #b.lname=request.POST.get('lname')
    # b.uname=request.POST.get('username')
    # b.email=request.POST.get('email')
    # pword=request.POST.get('password')
    # user = User.objects.create_user(username=b.uname, email=b.email, password=pword)
    # b.save()
    # return render(request, "index.html")


def loginDetails(request):
    if (request.method == "POST"):
        uname = request.POST.get('uname')
        pword = request.POST.get('password')
        user = auth.authenticate(username=uname, password=pword)

        if (user is not None):
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Invalid Username or password")
    return render(request, "index.html")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def profile(request):
    return render(request, "profile.html")


def product(request, kitcat):
        if(kitcat=='Beverages'):
                p=Beverages.objects.all()
        return render(request, "product.html", {"Product": p, "Kitchen": kitcat})




