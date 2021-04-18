"""Grocery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signupUser),
    path('login/', views.loginDetails),
    path('logout/', views.logout),
    path('product/<str:cat>/', views.product),
    path('profile/', views.profile),
    path('productinfo/<int:num>/<str:cat>/', views.productInfo),
    path('addbakery/', views.addBakery),
    path('addpulses/', views.addPulses),
    path('addsnacks/', views.addSnacks),
    path('addfruits/', views.addFruits),
    path('addvegetables/', views.addVegetables),
    path('addfrozenfood/', views.addFrozenfoods),
    path('addspices/', views.addSpices),
    path('addbeverages/', views.addBeverages),
    path('deleteproduct/<int:num>/<str:cat>/', views.deleteProduct),
    path('editproduct/<int:num>/<str:cat>/', views.editProduct),
    path('checkout/', views.checkOut),
    path('payment/', views.payment),
    path('contact/', views.contactDetails),
    path('cart/<int:num>/<str:cat>/', views.cart),
    path('cartdetails/', views.cartDetails),
    path('deletecart/<int:num>/', views.deleteCart),
    path('wishlist/<int:num>/<str:cat>/', views.wishlist),
    path('wishlistdetails/', views.wishlistDetails),
    path('deletewishlist/<int:num>/', views.wishlistDelete),
    path('checkout/', views.checkOut),
    path('payment/', views.payment),
    path('about/', views.aboutUs),


    #path('productinfo/<int:id>/', views.productInfo),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
