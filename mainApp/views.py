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
        { % extends
        'index.html' %}
        { % load
        static %}
        { % block
        body %}
        < div

        class ="privacy" >

        < div

        class ="container" >

        < !-- tittle
        heading -->
        < h3

        class ="tittle-w3l" > Personal Information

        < div

        class ="contact agileits" >

        < div

        class ="contact-agileinfo" >

        < div

        class ="contact-form wthree" >

        < p > Welcome < / p > < h2 > {{User.uname}} < / h2 >
        < br >
        < form
        method = "post" >
        { % csrf_token %}
        < div

        class ="" >

        < input
        type = "text"
        name = "name"
        placeholder = "Name"
        value = "{{User.name}}"
        required = "" >
    < / div >
    < div

    class ="" >

    < input

    class ="text" type="text" name="uname" placeholder="Username" value="{{User.uname}}" required="" >

< / div >
< div


class ="" >

< input


class ="email" type="email" name="email" placeholder="Email"  value="{{User.email}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="address1" placeholder="Address" value="{{User.address1}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="landmark" placeholder="Landmark" value="{{User.landmark}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="city" placeholder="City" value="{{User.city}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="state" placeholder="State" value="{{User.state}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="pin" placeholder="Pin" value="{{User.pin}}" required="" >

< / div >
< input
type = "submit"
value = "Update" >
< / form >
< / div >
< / h3 >
< div


class ="privacy" >

< div


class ="container" >

< !-- tittle
heading -->
< h3


class ="tittle-w3l" > Your Order History

< span


class ="heading-style" >

< i > < / i >
< i > < / i >
< i > < / i >
< / span >
< / h3 >

< div


class ="checkout-right" >

< h4 > Your
shopping
cart
contains:
< span > 3
Products < / span >
< / h4 >
< div


class ="table-responsive" >

< table


class ="timetable_sub" >

< thead >
< tr >
< th > SL
No. < / th >
< th > Product < / th >
< th > Quality < / th >
< th > Product
Name < / th >

< th > Price < / th >
< th > Remove < / th >
< / tr >
< / thead >
< tbody >
< tr


class ="rem1" >

< td


class ="invert" > 1 < / td >

< td


class ="invert-image" >

< a
href = "single2.html" >
< img
src = "images/a7.jpg"
alt = " "


class ="img-responsive" >

< / a >
< / td >
< td


class ="invert" >

< div


class ="quantity" >

< div


class ="quantity-select" >

< div


class ="entry value-minus" > & nbsp; < / div >

< div


class ="entry value" >

< span > 1 < / span >
< / div >
< div


class ="entry value-plus active" > & nbsp; < / div >

< / div >
< / div >
< / td >
< td


class ="invert" > Spotzero Spin Mop < / td >

< td


class ="invert" > $888.00 < / td >

< td


class ="invert" >

< div


class ="rem" >

< div


class ="close1" > < / div >

< / div >
< / td >
< / tr >
< tr


class ="rem2" >

< td


class ="invert" > 2 < / td >

< td


class ="invert-image" >

< a
href = "single2.html" >
< img
src = "images/s6.jpg"
alt = " "


class ="img-responsive" >

< / a >
< / td >
< td


class ="invert" >

< div


class ="quantity" >

< div


class ="quantity-select" >

< div


class ="entry value-minus" > & nbsp; < / div >

< div


class ="entry value" >

< span > 1 < / span >
< / div >
< div


class ="entry value-plus active" > & nbsp; < / div >

< / div >
< / div >
< / td >
< td


class ="invert" > Fair & Lovely, 80 g < / td >

< td


class ="invert" > $121.60 < / td >

< td


class ="invert" >

< div


class ="rem" >

< div


class ="close2" > < / div >

< / div >
< / td >
< / tr >
< tr


class ="rem3" >

< td


class ="invert" > 3 < / td >

< td


class ="invert-image" >

< a
href = "single.html" >
< img
src = "images/s5.jpg"
alt = " "


class ="img-responsive" >

< / a >
< / td >
< td


class ="invert" >

< div


class ="quantity" >

< div


class ="quantity-select" >

< div


class ="entry value-minus" > & nbsp; < / div >

< div


class ="entry value" >

< span > 1 < / span >
< / div >
< div


class ="entry value-plus active" > & nbsp; < / div >

< / div >
< / div >
< / td >
< td


class ="invert" > Sprite, 2.25L (Pack of 2) < / td >

< td


class ="invert" > $180.00 < / td >

< td


class ="invert" >

< div


class ="rem" >

< div


class ="close3" > < / div >

< / div >
< / td >
< / tr >
< / tbody >
< / table >

< / div >
< / div >
< div


class ="privacy" >

< div


class ="container" >

< !-- tittle
heading -->
< h3


class ="tittle-w3l" > Bank Details

< span


class ="heading-style" >

< i > < / i >
< i > < / i >
< i > < / i >
< / span >
< / h3 >

< !-- // checkout
page -->




{ % endblock %}
{ % extends
'index.html' %}
{ % load
static %}
{ % block
body %}
< div


class ="privacy" >

< div


class ="container" >

< !-- tittle
heading -->
< h3


class ="tittle-w3l" > Personal Information

< div


class ="contact agileits" >

< div


class ="contact-agileinfo" >

< div


class ="contact-form wthree" >

< p > Welcome < / p > < h2 > {{User.uname}} < / h2 >
< br >
< form
method = "post" >
{ % csrf_token %}
< div


class ="" >

< input
type = "text"
name = "name"
placeholder = "Name"
value = "{{User.name}}"
required = "" >
< / div >
< div


class ="" >

< input


class ="text" type="text" name="uname" placeholder="Username" value="{{User.uname}}" required="" >

< / div >
< div


class ="" >

< input


class ="email" type="email" name="email" placeholder="Email"  value="{{User.email}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="address1" placeholder="Address" value="{{User.address1}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="landmark" placeholder="Landmark" value="{{User.landmark}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="city" placeholder="City" value="{{User.city}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="state" placeholder="State" value="{{User.state}}" required="" >

< / div >
< div


class ="" >

< input


class ="text" type="text" name="pin" placeholder="Pin" value="{{User.pin}}" required="" >

< / div >
< input
type = "submit"
value = "Update" >
< / form >
< / div >
< / h3 >
< div


class ="privacy" >

< div


class ="container" >

< !-- tittle
heading -->
< h3


class ="tittle-w3l" > Your Order History

< span


class ="heading-style" >

< i > < / i >
< i > < / i >
< i > < / i >
< / span >
< / h3 >

< div


class ="checkout-right" >

< h4 > Your
shopping
cart
contains:
< span > 3
Products < / span >
< / h4 >
< div


class ="table-responsive" >

< table


class ="timetable_sub" >

< thead >
< tr >
< th > SL
No. < / th >
< th > Product < / th >
< th > Quality < / th >
< th > Product
Name < / th >

< th > Price < / th >
< th > Remove < / th >
< / tr >
< / thead >
< tbody >
< tr


class ="rem1" >

< td


class ="invert" > 1 < / td >

< td


class ="invert-image" >

< a
href = "single2.html" >
< img
src = "images/a7.jpg"
alt = " "


class ="img-responsive" >

< / a >
< / td >
< td


class ="invert" >

< div


class ="quantity" >

< div


class ="quantity-select" >

< div


class ="entry value-minus" > & nbsp; < / div >

< div


class ="entry value" >

< span > 1 < / span >
< / div >
< div


class ="entry value-plus active" > & nbsp; < / div >

< / div >
< / div >
< / td >
< td


class ="invert" > Spotzero Spin Mop < / td >

< td


class ="invert" > $888.00 < / td >

< td


class ="invert" >

< div


class ="rem" >

< div


class ="close1" > < / div >

< / div >
< / td >
< / tr >
< tr


class ="rem2" >

< td


class ="invert" > 2 < / td >

< td


class ="invert-image" >

< a
href = "single2.html" >
< img
src = "images/s6.jpg"
alt = " "


class ="img-responsive" >

< / a >
< / td >
< td


class ="invert" >

< div


class ="quantity" >

< div


class ="quantity-select" >

< div


class ="entry value-minus" > & nbsp; < / div >

< div


class ="entry value" >

< span > 1 < / span >
< / div >
< div


class ="entry value-plus active" > & nbsp; < / div >

< / div >
< / div >
< / td >
< td


class ="invert" > Fair & Lovely, 80 g < / td >

< td


class ="invert" > $121.60 < / td >

< td


class ="invert" >

< div


class ="rem" >

< div


class ="close2" > < / div >

< / div >
< / td >
< / tr >
< tr


class ="rem3" >

< td


class ="invert" > 3 < / td >

< td


class ="invert-image" >

< a
href = "single.html" >
< img
src = "images/s5.jpg"
alt = " "


class ="img-responsive" >

< / a >
< / td >
< td


class ="invert" >

< div


class ="quantity" >

< div


class ="quantity-select" >

< div


class ="entry value-minus" > & nbsp; < / div >

< div


class ="entry value" >

< span > 1 < / span >
< / div >
< div


class ="entry value-plus active" > & nbsp; < / div >

< / div >
< / div >
< / td >
< td


class ="invert" > Sprite, 2.25L (Pack of 2) < / td >

< td


class ="invert" > $180.00 < / td >

< td


class ="invert" >

< div


class ="rem" >

< div


class ="close3" > < / div >

< / div >
< / td >
< / tr >
< / tbody >
< / table >

< / div >
< / div >
< div


class ="privacy" >

< div


class ="container" >

< !-- tittle
heading -->
< h3


class ="tittle-w3l" > Bank Details

< span


class ="heading-style" >

< i > < / i >
< i > < / i >
< i > < / i >
< / span >
< / h3 >

< !-- // checkout
page -->




{ % endblock %}
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
    if(kitcat=='Frozen Foods'):
        p=FrozenFoods.objects.all()
    if(kitcat=='Pulses'):
        p=Pulses.objects.all()
    if(kitcat=='Vegetables'):
        p=Vegetables.objects.all()
    if(kitcat=='Fruits'):
        p=Fruits.objects.all()
    if(kitcat=='Snacks'):
        p=Snacks.objects.all()
    if(kitcat=='Spices'):
        p=Spices.objects.all()
    if(kitcat=='Bakery'):
        p=Bakery.objects.all()
    print("\n\n\n\n\n\n")
    print(kitcat)
    print("\n\n\n\n\n\n")
    return render(request, "product.html", {"Product": p, "Kitchen": kitcat})

# def productInfo(request, id):





