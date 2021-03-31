from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views 'here.
def home(request):
        return render(request, "index.html")


def signupUser(request):
        b=Buyer()
        b.name=request.POST.get('name')
        #b.lname=request.POST.get('lname')
        b.uname=request.POST.get('username')
        b.email=request.POST.get('email')
        pword=request.POST.get('password')
        user = User.objects.create_user(username=b.uname, email=b.email, password=pword)
        b.save()
        return render(request, "index.html")

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
