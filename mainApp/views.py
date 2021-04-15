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
    kit = KitchenCategory.objects.all()
    if (request.method == "POST"):
        uname = request.POST.get('uname')
        pword = request.POST.get('password')
        user = auth.authenticate(username=uname, password=pword)

        if (user is not None):
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Invalid Username or password")
    return render(request, "index.html", {"KitCat": kit})


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
            p.size = request.POST.get('size')
            p.quantity = request.POST.get('quantity')
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
            p.size = request.POST.get('size')
            p.quantity = request.POST.get('quantity')
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
            p.size = request.POST.get('size')
            p.quantity = request.POST.get('quantity')
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
            p.size = request.POST.get('size')
            p.quantity = request.POST.get('quantity')
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
            p.size = request.POST.get('size')
            p.quantity = request.POST.get('quantity')
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
            p.size = request.POST.get('size')
            p.quantity = request.POST.get('quantity')
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
            p.size = request.POST.get('size')
            p.quantity = request.POST.get('quantity')
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
            p.size = request.POST.get('size')
            p.quantity = request.POST.get('quantity')
            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addbeverages.html", {"KitCat": kit})


def cartDetails(request):
    kit = KitchenCategory.objects.all()
    if(request.user.is_anonymous):
        return HttpResponseRedirect('/login/')
    user = User.objects.get(username=request.user)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    try:
        Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        b = Buyer.objects.get(uname=request.user)
        cart = Cart.objects.filter(user=b)
        subtotal = 0
        for i in cart:
            subtotal += i.total
        if (subtotal < 1000):
            delivery = 150
        else:
            delivery = 0
        finalAmount = subtotal + delivery

    return render(request,"cart.html", {"KitCat": kit, "Cart": cart, "Sub": subtotal, "Delivery": delivery, "Final": finalAmount})



@login_required(login_url='/login/')
def cart(request, num, cat):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    kit = KitchenCategory.objects.all()
    if (request.method == 'POST'):
        try:
            c = Cart()
            if(cat=='Bakery'):
                c.bakery=Bakery.objects.get(id=num)
            if(cat=='Beverages'):
                c.beverages=Beverages.objects.get(id=num)
            if(cat=='Spices'):
                c.spices=Spices.objects.get(id=num)
            if(cat=='Snacks'):
                c.snacks=Snacks.objects.get(id=num)
            if(cat=='Pulses'):
                c.pulses=Pulses.objects.get(id=num)
            if (cat == 'Frozen Foods'):
                c.frozenFoods = FrozenFoods.objects.get(id=num)
            if (cat == 'Fruits'):
                c.fruits = Fruits.objects.get(id=num)
            if (cat == 'Vegetables'):
                c.vegetables = Vegetables.objects.get(id=num)
            c.user = Buyer.objects.get(uname=request.user)
            c.cat = KitchenCategory.objects.get(name=cat)
            c.quantity = int(request.POST.get('quantity'))
            print(type(c.quantity))
            c.finalPrice = int(request.POST.get('fprice'))
            c.total = c.finalPrice * c.quantity
            c.save()
            return HttpResponseRedirect('/cartdetails/')
        except:
            return HttpResponseRedirect('/login/')

    return render(request, "cart.html", {"KitCat": kit})


def deleteCart(request, num):
    user = User.objects.get(username=request.user)
    kit = KitchenCategory.objects.all()
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    cart = Cart.objects.get(id=num)
    cart.delete()
    return HttpResponseRedirect('/cartdetails/')


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
    dic={"Product":p, "KitCat": kit, "Quan": str(p.quantity)}
    return render(request, "productinfo.html", dic)


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
        p=Beverages.objects.get(id=num)
        if(request.method=='POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')

    if (cat == 'Vegetables'):
        veg = Vegetables.objects.get(id=num)
        if (request.method == 'POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')

    if (cat == 'Fruits'):
        p = Fruits.objects.get(id=num)
        if (request.method == 'POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')

    if (cat == 'Spices'):
        p = Spices.objects.get(id=num)
        if (request.method == 'POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')

    if (cat == 'Snacks'):
        p = Snacks.objects.get(id=num)
        if (request.method == 'POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')

    if (cat == 'Bakery'):
        p = Bakery.objects.get(id=num)
        if (request.method == 'POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')

    if (cat == 'Pulses'):
        p = Pulses.objects.get(id=num)
        if (request.method == 'POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')

    if (cat == 'FrozenFoods'):
        p = FrozenFoods.objects.get(id=num)
        if (request.method == 'POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
    return render(request, "editproduct.html", {"Product":p,"KitCat": kit})


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
        w = WishList()
        w.frozenFoods = FrozenFoods.objects.get(id=num)
        w.bakery = Bakery.objects.get(id=num)
        w.spices = Spices.objects.get(id=num)
        w.pulses = Pulses.objects.get(id=num)
        w.vegetables = Vegetables.objects.get(id=num)
        w.snacks = Snacks.objects.get(id=num)
        w.fruits = Fruits.objects.get(id=num)
        w.beverages = Beverages.objects.get(id=num)
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
        wish = WishList.objects.filter(user=user)
        return render(request, "wishlist.html",
                      {"Wish": wish})


@login_required(login_url='/login/')
def wishlistDelete(request, num):
    wish = WishList.objects.get(id=num)
    wish.delete()
    return HttpResponseRedirect('/wishlist/')


def checkOut(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    try:
        user = Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        user = Buyer.objects.get(uname=request.user)
        if (request.method == "POST"):
            t=0
            ch = CheckOut()
            ch.user = user
            ch.address1 = request.POST.get('address1')
            ch.pin = request.POST.get('pin')
            ch.state = request.POST.get('state')
            ch.city = request.POST.get('city')
            ch.name = request.POST.get('name')
            ch.email = request.POST.get('email')
            ch.phone = request.POST.get('phone')
            cart = Cart.objects.filter(user=user)
            for i in cart:
                t = t + i.total
                order=OrdersPlaced()
                if(i.cat==KitchenCategory.objects.get(name='Fruits')):
                    print("\n\n\n\n\n\n")
                    # f=i.fruits
                    # print(type(f))
                    order.user = i.user
                    order.fruits = i.fruits
                    print("\n\n\n\nn\n\n\n hello")
                    order.quantity = i.quantity
                    order.finalPrice = i.finalPrice
                    order.save()
            if(t<1000):
                t+=150
            ch.total = t
            ch.save()
            cart.delete()
            return HttpResponseRedirect('/payment/')
        return render(request, "checkout.html", {"User": user})


def payment(request):
    return render(request, "payment.html")