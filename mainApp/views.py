from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
        kit = KitchenCategory.objects.all()
        return render(request, "index.html", {"KitCat": kit})


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
    kit = KitchenCategory.objects.all()
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        try:
            s = Seller.objects.get(uname=request.user)
            print("/n/n/n/n/n/n/n/n/nhello")
            bakery = Bakery.objects.filter(seller_details=s)
            spices = Spices.objects.filter(seller_details=s)
            snacks = Snacks.objects.filter(seller_details=s)
            frozenfoods = FrozenFoods.objects.filter(seller_details=s)
            vegetables = Vegetables.objects.filter(seller_details=s)
            fruits = Fruits.objects.filter(seller_details=s)
            beverages = Beverages.objects.filter(seller_details=s)
            pulses = Pulses.objects.filter(seller_details=s)
            if (request.method == "POST"):
                s.name = request.POST.get('name')
                s.uname = request.POST.get('uname')
                s.email = request.POST.get('email')
                s.phone = request.POST.get('phone')
                s.address = request.POST.get('address')
                s.city = request.POST.get('city')
                s.save()
                return HttpResponseRedirect('/profile/')
            return render(request, "seller.html", {
                "User": s,
                "KitCat": kit,
                "Bakery":bakery,
                "Spices":spices,
                "Snacks":snacks,
                "Beverages":beverages,
                "Vegetables":vegetables,
                "Fruits":fruits,
                "FrozenFoods":frozenfoods,
                "Pulses":pulses
            })
        except:
            b = Buyer.objects.get(uname=request.user)
            if (request.method == "POST"):
                b.name = request.POST.get('name')
                b.uname = request.POST.get('uname')
                b.email = request.POST.get('email')
                b.address1 = request.POST.get('address1')
                b.landmark = request.POST.get('landmark')
                b.city = request.POST.get('city')
                b.state = request.POST.get('state')
                b.pin = request.POST.get('pin')
                b.bankName = request.POST.get('bankName')
                b.accountNumber = request.POST.get('accountNumber')
                b.save()
                return HttpResponseRedirect('/profile/')
            return render(request, "buyer.html", {"User": b, "KitCat": kit})

def product(request, cat):
    kit = KitchenCategory.objects.all()
    if(cat=='Beverages'):
        p=Beverages.objects.all()
    if(cat=='Frozen Foods'):
        p=FrozenFoods.objects.all()
    if(cat=='Pulses'):
        p=Pulses.objects.all()
    if(cat=='Vegetables'):
        p=Vegetables.objects.all()
    if(cat=='Fruits'):
        p=Fruits.objects.all()
    if(cat=='Snacks'):
        p=Snacks.objects.all()
    if(cat=='Spices'):
        p=Spices.objects.all()
    if(cat=='Bakery'):
        p=Bakery.objects.all()
    return render(request, "product.html", {"Product": p, "Category": cat, "KitCat": kit})


def productInfo(request, num, cat):
    kit = KitchenCategory.objects.all()
    print("\n\n\n")
    print(cat)
    if(cat=='FrozenFoods'):
        p=FrozenFoods.objects.get(id=num)
    if(cat=='Fruits'):
        p=Fruits.objects.get(id=num)
    if(cat=='Beverages'):
        p=Beverages.objects.get(id=num)
    if(cat=='Spices'):
        p=Spices.objects.get(id=num)
    if(cat=='Pulses'):
        p=Pulses.objects.get(id=num)
    if(cat=='Vegetables'):
        p=Vegetables.objects.get(id=num)
    if(cat=='Bakery'):
        p=Bakery.objects.get(id=num)
    if(cat=='Snacks'):
        p=Snacks.objects.get(id=num)
    return render(request, "productinfo.html", {"Product":p, "KitCat": kit})

def addBakery(request):
    kit = KitchenCategory.objects.all()
    user= User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    if(request.method=='POST'):
        try:
            s = Seller.objects.get(uname=request.user)
            p=Bakery()
            p.name=request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int( request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice=p.basePrice-(p.basePrice*int(p.discount))//100
            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addbakery.html", {"KitCat": kit})

def addPulses(request):
    kit = KitchenCategory.objects.all()
    user= User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    if(request.method=='POST'):
        try:
            s = Seller.objects.get(uname=request.user)
            p=Pulses()
            p.name=request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int( request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice=p.basePrice-(p.basePrice*int(p.discount))//100

            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addpulses.html", {"KitCat": kit})

def addSnacks(request):
    kit = KitchenCategory.objects.all()
    user= User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    if(request.method=='POST'):
        try:
            s = Seller.objects.get(uname=request.user)
            p=Snacks()
            p.name=request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int( request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice=p.basePrice-(p.basePrice*int(p.discount))//100

            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addsnacks.html", {"KitCat": kit})

def addFruits(request):
    kit = KitchenCategory.objects.all()
    user= User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    if(request.method=='POST'):
        try:
            s = Seller.objects.get(uname=request.user)
            p=Fruits()
            p.name=request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int( request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice=p.basePrice-(p.basePrice*int(p.discount))//100

            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addfruits.html", {"KitCat": kit})

def addVegetables(request):
    kit = KitchenCategory.objects.all()
    user= User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    if(request.method=='POST'):
        try:
            s = Seller.objects.get(uname=request.user)
            p=Vegetables()
            p.name=request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int( request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice=p.basePrice-(p.basePrice*int(p.discount))//100

            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addvegetables.html", {"KitCat": kit})


def addFrozenfoods(request):
    kit = KitchenCategory.objects.all()
    user= User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    if(request.method=='POST'):
        try:
            s = Seller.objects.get(uname=request.user)
            p=FrozenFoods()
            p.name=request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int( request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice=p.basePrice-(p.basePrice*int(p.discount))//100

            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addfrozenfood.html", {"KitCat": kit})

def addSpices(request):
    kit = KitchenCategory.objects.all()
    user= User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    if(request.method=='POST'):
        try:
            s = Seller.objects.get(uname=request.user)
            p=Spices()
            p.name=request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int( request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice=p.basePrice-(p.basePrice*int(p.discount))//100

            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addspices.html", {"KitCat": kit})

def addBeverages(request):
    kit = KitchenCategory.objects.all()
    user= User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    if(request.method=='POST'):
        try:
            s = Seller.objects.get(uname=request.user)
            p=Beverages()
            p.name=request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int( request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice=p.basePrice-(p.basePrice*int(p.discount))//100


            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addbeverages.html", {"KitCat": kit})


def cart(request):
    kit = KitchenCategory.objects.all()
    return render(request, "cart.html", {"KitCat": kit})



def productInfo(request, num, cat):
    kit = KitchenCategory.objects.all()
    if(cat=='FrozenFoods'):
        p=FrozenFoods.objects.get(id=num)
    if(cat=='Fruits'):
        p=Fruits.objects.get(id=num)
    if(cat=='Beverages'):
        p=Beverages.objects.get(id=num)
    if(cat=='Spices'):
        p=Spices.objects.get(id=num)
    if(cat=='Pulses'):
        p=Pulses.objects.get(id=num)
    if(cat=='Vegetables'):
        p=Vegetables.objects.get(id=num)
    if(cat=='Bakery'):
        p=Bakery.objects.get(id=num)
    if(cat=='Snacks'):
        p=Snacks.objects.get(id=num)
    return render(request, "productinfo.html", {"Product":p, "KitCat": kit})

def deleteProduct(request, num, cat):
    user = User.objects.get(username=request.user)
    kit = KitchenCategory.objects.all()
    if(cat=='FrozenFoods'):
        p=FrozenFoods.objects.get(id=num)
        p.delete()
    if(cat=='Fruits'):
        p=Fruits.objects.get(id=num)
        p.delete()
    if(cat=='Beverages'):
        p=Beverages.objects.get(id=num)
        p.delete()
    if(cat=='Spices'):
        p=Spices.objects.get(id=num)
        p.delete()
    if(cat=='Pulses'):
        p=Pulses.objects.get(id=num)
        p.delete()
    if(cat=='Vegetables'):
        p=Vegetables.objects.get(id=num)
        p.delete()
    if(cat=='Bakery'):
        p=Bakery.objects.get(id=num)
        p.delete()
    if(cat=='Snacks'):
        p=Snacks.objects.get(id=num)
        p.delete()
    return HttpResponseRedirect('/profile/')
    # return render(request, "seller.html", {"Product":p, "KitCat": kit})

def editProduct(request,num, cat):
    user = User.objects.get(username=request.user)
    kit = KitchenCategory.objects.all()
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    if(cat=='Beverages'):
        bev=Beverages.objects.get(id=num)
        if(request.method=='POST'):
            s = Seller.objects.get(uname=request.user)
            bev.name = request.POST.get('name')
            bev.desc = request.POST.get('description')
            bev.basePrice = int(request.POST.get('baseprice'))
            bev.discount = request.POST.get('discount')
            bev.finalPrice = bev.basePrice - bev.basePrice * int(bev.discount) // 100
            bev.seller = s
            bev.save()
            return HttpResponseRedirect('/profile/')
        return render(request,"editproduct.html",{"Product":bev,"KitCat": kit})

@login_required(login_url='/login/')
def wishlistDetails(request, num):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin')
    try:
        user = Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        user = Buyer.objects.get(uname=request.user)
        w = wishlist()
        FrozenFoods = FrozenFoods.objects.get(id=num)
        Bakery = Bakery.objects.get(id=num)
        Spices = Spices.objects.get(id=num)
        Pulses = Pulses.objects.get(id=num)
        Vegetables = Vegetables.objects.get(id=num)
        Snacks = Snacks.objects.get(id=num)
        Fruits = Fruits.objects.get(id=num)
        Beverages = Beverages.objects.get(id=num)
        w.user = user
        w.product = product
        w.save()
        return HttpResponseRedirect('/profile/')


@login_required(login_url='/login/')
def wishlistBuyer(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin')
    try:
        user = Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        user = Buyer.objects.get(uname=request.user)
        wish = wishlist.objects.filter(user=user)
        return render(request, "wishlist.html",
                      {"Wish": wish})


@login_required(login_url='/login/')
def wishlistDelete(request, num):
    wish = wishlist.objects.get(id=num)
    wish.delete()
    return HttpResponseRedirect('/wishlist/')
