from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    kit = KitchenCategory.objects.all()     #to get all the kitchen categories
    return render(request, "index.html", {"KitCat": kit})


def signupUser(request):
    choice = request.POST.get('option') #to get the value of option field from signup from.
    if (choice == 'seller'):
        s = Seller()
        s.name = request.POST.get('name')
        s.uname = request.POST.get('username')
        s.email = request.POST.get('email')
        pword = request.POST.get('password')
        try:
            user = User.objects.create_user(
                username=s.uname, email=s.email, password=pword)        #creates user
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
            bakery = Bakery.objects.filter(seller_details=s)
            spices = Spices.objects.filter(seller_details=s)
            snacks = Snacks.objects.filter(seller_details=s)
            frozenfoods = FrozenFoods.objects.filter(seller_details=s)
            vegetables = Vegetables.objects.filter(seller_details=s)
            fruits = Fruits.objects.filter(seller_details=s)
            beverages = Beverages.objects.filter(seller_details=s)
            pulses = Pulses.objects.filter(seller_details=s)
            orders = OrdersPlaced.objects.filter(seller_details = s)
            if (request.method == "POST"):              #to update the seller information
                s.name = request.POST.get('name')
                s.uname = request.POST.get('uname')
                s.email = request.POST.get('email')
                s.phone = request.POST.get('phone')
                s.address = request.POST.get('address')
                s.city = request.POST.get('city')
                s.pin = request.POST.get('pin')
                s.state = request.POST.get('state')
                s.landmark = request.POST.get('landmark')
                s.bankName = request.POST.get('bankName')
                s.ifscCode = request.POST.get('ifscCode')
                s.accountNumber = request.POST.get('accountNumber')
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
                "Pulses":pulses,
                "Order":orders,
            })
        except:
            b = Buyer.objects.get(uname=request.user)
            order = OrdersPlaced.objects.filter(user = b)
            if (request.method == "POST"):          #to update the buyer information
                b.name = request.POST.get('name')
                b.uname = request.POST.get('uname')
                b.email = request.POST.get('email')
                b.phone = request.POST.get('phone')
                b.address = request.POST.get('address')
                b.landmark = request.POST.get('landmark')
                b.city = request.POST.get('city')
                b.state = request.POST.get('state')
                b.pin = request.POST.get('pin')
                b.bankName = request.POST.get('bankName')
                b.accountNumber = request.POST.get('accountNumber')
                b.save()
                return HttpResponseRedirect('/profile/')
            return render(request, "buyer.html", {"User": b, "KitCat": kit, "Order": order})


def product(request, cat):              #to display the products according to the category
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
            if(int(p.quantity)>0):
                p.stock=True
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
            if (int(p.quantity) > 0):
                p.stock = True
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
            if (int(p.quantity) > 0):
                p.stock = True
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
            if (int(p.quantity) > 0):
                p.stock = True
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
            if (int(p.quantity) > 0):
                p.stock = True
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
            if (int(p.quantity) > 0):
                p.stock = True
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
            if (int(p.quantity) > 0):
                p.stock = True
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
            if (int(p.quantity) > 0):
                p.stock = True
            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addbeverages.html", {"KitCat": kit})


@login_required(login_url='/login/')
def cart(request, num, cat):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    kit = KitchenCategory.objects.all()
    if (request.method == 'POST'):
        try:
            if(cat == 'Fruits'):
                try:            #if the item is already present in cart
                    c = Cart.objects.get(fruits = num)
                    q = int(request.POST.get('quantity'))       #gets the quantity entered by the buyer
                    c.quantity = c.quantity + q                 #adds the quantity to already added and new quantity
                    quan = c.fruits.quantity                    #gets the quantity available or stock avaialble
                    if (c.quantity > quan):
                        c.quantity = quan                       #sets the maximum quantity to available quantity
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')
                except:             #if the item is not present in cart, then it creates a new one
                    c = Cart()
                    c.fruits = Fruits.objects.get(id=num)
                    c.user = Buyer.objects.get(uname=request.user)
                    c.cat = KitchenCategory.objects.get(name=cat)
                    c.quantity = int(request.POST.get('quantity'))
                    c.finalPrice = int(request.POST.get('fprice'))
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')

            if (cat == 'Beverages'):
                try:
                    c = Cart.objects.get(beverages=num)
                    q = int(request.POST.get('quantity'))
                    c.quantity = c.quantity + q
                    quan = c.beverages.quantity
                    if(c.quantity  > quan):
                        c.quantity = quan
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')
                except:
                    c = Cart()
                    c.beverages = Beverages.objects.get(id=num)
                    c.user = Buyer.objects.get(uname=request.user)
                    c.cat = KitchenCategory.objects.get(name=cat)
                    c.quantity = int(request.POST.get('quantity'))
                    c.finalPrice = int(request.POST.get('fprice'))
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')

            if (cat == 'Snacks'):
                try:
                    c = Cart.objects.get(snacks=num)
                    q = int(request.POST.get('quantity'))
                    c.quantity = c.quantity + q
                    quan = c.snacks.quantity
                    if (c.quantity > quan):
                        c.quantity = quan
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')
                except:
                    c = Cart()
                    c.snacks = Snacks.objects.get(id=num)
                    c.user = Buyer.objects.get(uname=request.user)
                    c.cat = KitchenCategory.objects.get(name=cat)
                    c.quantity = int(request.POST.get('quantity'))
                    c.finalPrice = int(request.POST.get('fprice'))
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')

            if (cat == 'Spices'):
                try:
                    c = Cart.objects.get(spices=num)
                    q = int(request.POST.get('quantity'))
                    c.quantity = c.quantity + q
                    quan = c.spices.quantity
                    if (c.quantity > quan):
                        c.quantity = quan
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')
                except:
                    c = Cart()
                    c.spices = Spices.objects.get(id=num)
                    c.user = Buyer.objects.get(uname=request.user)
                    c.cat = KitchenCategory.objects.get(name=cat)
                    c.quantity = int(request.POST.get('quantity'))
                    c.finalPrice = int(request.POST.get('fprice'))
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')

            if (cat == 'Vegetables'):
                try:
                    c = Cart.objects.get(vegetables=num)
                    q = int(request.POST.get('quantity'))
                    c.quantity = c.quantity + q
                    quan = c.vegetables.quantity
                    if (c.quantity > quan):
                        c.quantity = quan
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')
                except:
                    c = Cart()
                    c.vegetables = Vegetables.objects.get(id=num)
                    c.user = Buyer.objects.get(uname=request.user)
                    c.cat = KitchenCategory.objects.get(name=cat)
                    c.quantity = int(request.POST.get('quantity'))
                    c.finalPrice = int(request.POST.get('fprice'))
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')

            if (cat == 'Bakery'):
                try:
                    c = Cart.objects.get(bakery=num)
                    q = int(request.POST.get('quantity'))
                    c.quantity = c.quantity + q
                    quan = c.bakery.quantity
                    if (c.quantity > quan):
                        c.quantity = quan
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')
                except:
                    c = Cart()
                    c.bakery = Bakery.objects.get(id=num)
                    c.user = Buyer.objects.get(uname=request.user)
                    c.cat = KitchenCategory.objects.get(name=cat)
                    c.quantity = int(request.POST.get('quantity'))
                    c.finalPrice = int(request.POST.get('fprice'))
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')

            if (cat == 'Pulses'):
                try:
                    c = Cart.objects.get(pulses=num)
                    q = int(request.POST.get('quantity'))
                    c.quantity = c.quantity + q
                    quan = c.pulses.quantity
                    if (c.quantity > quan):
                        c.quantity = quan
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')
                except:
                    c = Cart()
                    c.pulses = Pulses.objects.get(id=num)
                    c.user = Buyer.objects.get(uname=request.user)
                    c.cat = KitchenCategory.objects.get(name=cat)
                    c.quantity = int(request.POST.get('quantity'))
                    c.finalPrice = int(request.POST.get('fprice'))
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')

            if (cat == 'Frozen Foods'):
                try:
                    c = Cart.objects.get(frozenFoods=num)
                    q = int(request.POST.get('quantity'))
                    quan = c.frozenFoods.quantity
                    if (c.quantity > quan):
                        c.quantity = quan
                    c.quantity = c.quantity + q
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')
                except:
                    c = Cart()
                    c.frozenFoods = FrozenFoods.objects.get(id=num)
                    c.user = Buyer.objects.get(uname=request.user)
                    c.cat = KitchenCategory.objects.get(name=cat)
                    c.quantity = int(request.POST.get('quantity'))
                    c.finalPrice = int(request.POST.get('fprice'))
                    c.total = c.finalPrice * c.quantity
                    c.save()
                    return HttpResponseRedirect('/cartdetails/')

        except:
            return HttpResponseRedirect('/login/')

    return render(request, "cart.html", {"KitCat": kit})


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
        if (subtotal < 500):            #checks for delivery charges
            delivery = 150
        else:
            delivery = 0
        finalAmount = subtotal + delivery
        return render(request,"cart.html", {"KitCat": kit, "Cart": cart, "Sub": subtotal, "Delivery": delivery, "Final": finalAmount})


def deleteCart(request, num):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    cart = Cart.objects.get(id=num)
    cart.delete()
    return HttpResponseRedirect('/cartdetails/')


def productInfo(request, num, cat):
    kit = KitchenCategory.objects.all()
    if (cat == 'Beverages' or cat == '1'):
        p = Beverages.objects.get(id=num)
    if(cat=='Pulses' or cat=='2'):
        p=Pulses.objects.get(id=num)
    if(cat=='Vegetables' or cat=='3'):
        p=Vegetables.objects.get(id=num)
    if(cat=='Fruits' or cat=='4'):
        p=Fruits.objects.get(id=num)
    if(cat=='Snacks' or cat=='5'):
        p=Snacks.objects.get(id=num)
    if (cat == 'Spices' or cat == '6'):
        p = Spices.objects.get(id=num)
    if (cat == 'Bakery' or cat == '7'):
        p = Bakery.objects.get(id=num)
    if(cat=='Frozen Foods' or cat=='8'):
        p=FrozenFoods.objects.get(id=num)
    dic={"Product":p, "KitCat": kit, "Quan": str(p.quantity)}
    return render(request, "productinfo.html", dic)


def deleteProduct(request, num, cat):
    user = User.objects.get(username=request.user)
    kit = KitchenCategory.objects.all()
    if(cat=='Frozen Foods'):
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
        p=Beverages.objects.get(id=num)             #fetches the product infromation from beverages model
        if(request.method=='POST'):
            s = Seller.objects.get(uname=request.user)          #fetches the seller infromation from the seller model
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.quantity = request.POST.get('quantity')
            if (int(p.quantity) > 0):
                p.stock = True
            else:
                p.stock = False
            p.seller_details = s
            p.save()            #saves changes of the product in the database
            return HttpResponseRedirect('/profile/')

    if (cat == 'Vegetables'):
        p = Vegetables.objects.get(id=num)
        if (request.method == 'POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.quantity = request.POST.get('quantity')
            if (int(p.quantity) > 0):
                p.stock = True
            else:
                p.stock = False
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
            p.quantity = request.POST.get('quantity')
            if (int(p.quantity) > 0):
                p.stock = True
            else:
                p.stock = False
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
            p.quantity = request.POST.get('quantity')
            if (int(p.quantity) > 0):
                p.stock = True
            else:
                p.stock = False
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
            p.quantity = request.POST.get('quantity')
            if (int(p.quantity) > 0):
                p.stock = True
            else:
                p.stock = False
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
            p.quantity = request.POST.get('quantity')
            if (int(p.quantity) > 0):
                p.stock = True
            else:
                p.stock = False
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
            p.quantity = request.POST.get('quantity')
            if (int(p.quantity) > 0):
                p.stock = True
            else:
                p.stock = False
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')

    if (cat == 'Frozen Foods'):
        p = FrozenFoods.objects.get(id=num)
        if (request.method == 'POST'):
            s = Seller.objects.get(uname=request.user)
            p.name = request.POST.get('name')
            p.desc = request.POST.get('description')
            p.basePrice = int(request.POST.get('baseprice'))
            p.discount = request.POST.get('discount')
            p.finalPrice = p.basePrice - p.basePrice * int(p.discount) // 100
            p.quantity = request.POST.get('quantity')
            if (int(p.quantity) > 0):
                p.stock = True
            else:
                p.stock = False
            p.seller_details = s
            p.save()
            return HttpResponseRedirect('/profile/')
    return render(request, "editproduct.html", {"Product":p,"KitCat": kit})


@login_required(login_url='/login/')
def wishlist(request, num, cat):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    kit = KitchenCategory.objects.all()
    if (request.method == 'POST'):
        try:
            w = WishList()
            if (cat == 'Bakery'):
                w.bakery = Bakery.objects.get(id=num)
            if (cat == 'Beverages'):
                w.beverages = Beverages.objects.get(id=num)
            if (cat == 'Spices'):
                w.spices = Spices.objects.get(id=num)
            if (cat == 'Snacks'):
                w.snacks = Snacks.objects.get(id=num)
            if (cat == 'Pulses'):
                w.pulses = Pulses.objects.get(id=num)
            if (cat == 'Frozen Foods'):
                w.frozenFoods = FrozenFoods.objects.get(id=num)
                print(w.frozenFoods)
            if (cat == 'Fruits'):
                w.fruits = Fruits.objects.get(id=num)
            if (cat == 'Vegetables'):
                w.vegetables = Vegetables.objects.get(id=num)
            w.user = Buyer.objects.get(uname=request.user)
            w.cat = KitchenCategory.objects.get(name=cat)
            w.save()
            return HttpResponseRedirect('/wishlistdetails/')
        except:
            return HttpResponseRedirect('/login/')
    return render(request, "wishlist.html", {"KitCat": kit})


@login_required(login_url='/login/')
def wishlistDetails(request):
    user = User.objects.get(username=request.user)
    kit = KitchenCategory.objects.all()
    if (user.is_superuser):
        return HttpResponseRedirect('/admin')
    try:
        user = Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        user = Buyer.objects.get(uname=request.user)
        wish = WishList.objects.filter(user=user)
        return render(request, "wishlist.html",
                      {"Wish": wish, "KitCat": kit})


@login_required(login_url='/login/')
def wishlistDelete(request, num):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    wish = WishList.objects.get(id=num)
    wish.delete()
    return HttpResponseRedirect('/wishlistdetails/')


def checkOut(request):
    user = User.objects.get(username=request.user)
    kit = KitchenCategory.objects.all()
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    try:
        user = Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        user = Buyer.objects.get(uname=request.user)
        if (request.method == "POST"):
            t=0                     #initializes total amount as 0
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
            for i in cart:          #to access all the items in cart
                t = t + i.total     #calculates the total amount to be paid
                order=OrdersPlaced()
                if(i.cat == KitchenCategory.objects.get(name = 'Fruits')):
                    order.user = i.user
                    order.fruits = i.fruits
                    order.seller_details = i.fruits.seller_details
                    order.quantity = i.quantity
                    order.finalPrice = i.total
                    order.save()
                    p = Fruits.objects.get(id=i.fruits.id)          #updates the stock of each item in database
                    p.quantity = p.quantity - i.quantity
                    if (int(p.quantity) > 0):
                        p.stock = True
                    else:
                        p.stock = False
                    p.save()
                if (i.cat == KitchenCategory.objects.get(name='Bakery')):
                    order.user = i.user
                    order.bakery = i.bakery
                    order.seller_details = i.bakery.seller_details
                    order.quantity = i.quantity
                    order.finalPrice = i.total
                    order.save()
                    p = Bakery.objects.get(id=i.bakery.id)
                    p.quantity = p.quantity - i.quantity
                    if (int(p.quantity) > 0):
                        p.stock = True
                    else:
                        p.stock = False
                    p.save()
                if (i.cat == KitchenCategory.objects.get(name='Spices')):
                    order.user = i.user
                    order.spices = i.spices
                    order.seller_details = i.spices.seller_details
                    order.quantity = i.quantity
                    order.finalPrice = i.total
                    order.save()
                    p = Spices.objects.get(id=i.spices.id)
                    p.quantity = p.quantity - i.quantity
                    if (int(p.quantity) > 0):
                        p.stock = True
                    else:
                        p.stock = False
                    p.save()
                if (i.cat == KitchenCategory.objects.get(name='Snacks')):
                    order.user = i.user
                    order.snacks = i.snacks
                    order.seller_details = i.snacks.seller_details
                    order.quantity = i.quantity
                    order.finalPrice = i.total
                    order.save()
                    p = Snacks.objects.get(id=i.snacks.id)
                    p.quantity = p.quantity - i.quantity
                    if (int(p.quantity) > 0):
                        p.stock = True
                    else:
                        p.stock = False
                    p.save()
                if (i.cat == KitchenCategory.objects.get(name='Beverages')):
                    order.user = i.user
                    order.beverages = i.beverages
                    order.seller_details = i.beverages.seller_details
                    order.quantity = i.quantity
                    order.finalPrice = i.total
                    order.save()
                    p = Beverages.objects.get(id=i.beverages.id)
                    p.quantity = p.quantity - i.quantity
                    if (int(p.quantity) > 0):
                        p.stock = True
                    else:
                        p.stock = False
                    p.save()
                if (i.cat == KitchenCategory.objects.get(name='Pulses')):
                    order.user = i.user
                    order.pulses = i.pulses
                    order.seller_details = i.pulses.seller_details
                    order.quantity = i.quantity
                    order.finalPrice = i.total
                    order.save()
                    p = Pulses.objects.get(id=i.pulses.id)
                    p.quantity = p.quantity - i.quantity
                    if (int(p.quantity) > 0):
                        p.stock = True
                    else:
                        p.stock = False
                    p.save()
                if (i.cat == KitchenCategory.objects.get(name='Frozen Foods')):
                    order.user = i.user
                    order.frozenFoods = i.frozenFoods
                    order.seller_details = i.frozenFoods.seller_details
                    order.quantity = i.quantity
                    order.finalPrice = i.total
                    order.save()
                    p = FrozenFoods.objects.get(id=i.frozenFoods.id)
                    p.quantity = p.quantity - i.quantity
                    if (int(p.quantity) > 0):
                        p.stock = True
                    else:
                        p.stock = False
                    p.save()
                if (i.cat == KitchenCategory.objects.get(name='Vegetables')):
                    order.user = i.user
                    order.vegetables = i.vegetables
                    order.seller_details = i.vegetables.seller_details
                    order.quantity = i.quantity
                    order.finalPrice = i.total
                    order.save()
                    p = Vegetables.objects.get(id=i.vegetables.id)
                    p.quantity = p.quantity - i.quantity
                    if (int(p.quantity) > 0):
                        p.stock = True
                    else:
                        p.stock = False
                    p.save()
            if(t<500):              #if total amount to be paid is less than 500, add delivery charges
                t+=150
            ch.total = t            #sets the total checkout amount
            ch.save()
            cart.delete()           #deletes the cart items after placing the order
            return HttpResponseRedirect('/payment/')
        return render(request, "checkout.html", {"User": user, "KitCat":kit})


def payment(request):
    user = User.objects.get(username=request.user)
    kit = KitchenCategory.objects.all()
    return render(request, "payment.html", {"User": user, "KitCat":kit})



def contactDetails(request):
    if(request.method == "POST"):
        c = Contact()
        c.name = request.POST.get('name')
        c.email = request.POST.get('email')
        c.subject = request.POST.get('subject')
        c.msg = request.POST.get('message')
        c.save()
        messages.success(request, "Message Sent")
        return HttpResponseRedirect('/contact/')

    return render(request, "contact.html")


def aboutUs(request):
    kit = KitchenCategory.objects.all()
    return render(request, "about.html", {"KitCat": kit})