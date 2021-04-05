from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    #lname = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default=None, null=True, blank=True)
    address1 = models.CharField(max_length=20, default=None, null=True, blank=True)
    landmark = models.CharField(max_length=20, default=None, null=True, blank=True)
    city = models.CharField(max_length=20, default=None, null=True, blank=True)
    state = models.CharField(max_length=20, default=None, null=True, blank=True)
    pin = models.CharField(max_length=20, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.name


class Seller(models.Model):
    name = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return str(self.id) + " " + self.name


class FrozenFoods(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    gm100 = models.BooleanField(default=None, blank=True, null=True)
    gm250 = models.BooleanField(default=None, blank=True, null=True)
    gm500 = models.BooleanField(default=None, blank=True, null=True)
    kg1 = models.BooleanField(default=None, blank=True, null=True)
    gm100_quan = models.IntegerField(default=0, null=True, blank=True)
    gm250_quan = models.IntegerField(default=0, null=True, blank=True)
    gm500_quan = models.IntegerField(default=0, null=True, blank=True)
    kg1_quan = models.IntegerField(default=0, null=True, blank=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.name


class Bakery(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    gm100 = models.BooleanField(default=None, blank=True, null=True)
    gm250 = models.BooleanField(default=None, blank=True, null=True)
    gm500 = models.BooleanField(default=None, blank=True, null=True)
    kg1 = models.BooleanField(default=None, blank=True, null=True)
    gm100_quan = models.IntegerField(default=0, null=True, blank=True)
    gm250_quan = models.IntegerField(default=0, null=True, blank=True)
    gm500_quan = models.IntegerField(default=0, null=True, blank=True)
    kg1_quan = models.IntegerField(default=0, null=True, blank=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.name


class Pulses(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    gm100 = models.BooleanField(default=None, blank=True, null=True)
    gm250 = models.BooleanField(default=None, blank=True, null=True)
    gm500 = models.BooleanField(default=None, blank=True, null=True)
    kg1 = models.BooleanField(default=None, blank=True, null=True)
    gm100_quan = models.IntegerField(default=0, null=True, blank=True)
    gm250_quan = models.IntegerField(default=0, null=True, blank=True)
    gm500_quan = models.IntegerField(default=0, null=True, blank=True)
    kg1_quan = models.IntegerField(default=0, null=True, blank=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.name


class Spices(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    gm100 = models.BooleanField(default=None, blank=True, null=True)
    gm100_quan = models.IntegerField(default=0, blank=True, null=True)
    gm250 = models.BooleanField(default=None, blank=True, null=True)
    gm250_quan = models.IntegerField(default=0, blank=True, null=True)
    gm500= models.BooleanField(default=None, blank=True, null=True)
    gm500_quan= models.IntegerField(default=0, blank=True, null=True)
    kg1 = models.BooleanField(default=None, blank=True, null=True)
    kg1_quan = models.IntegerField(default=0, blank=True, null=True)
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    seller_details=models.ForeignKey(Seller,on_delete=models.CASCADE)


class Vegetables(models.Model):
    name= models.CharField(max_length=50)
    quantity=models.IntegerField()
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    gm100=models.BooleanField(default=False, blank=True, null=True)
    gm100_quan = models.IntegerField(default=0, null=True, blank=True)
    gm250=models.BooleanField(default=False, blank=True, null=True)
    gm250_quan = models.IntegerField(default=0, null=True, blank=True)
    gm500=models.BooleanField(default=False, blank=True, null=True)
    gm500_quan = models.IntegerField(default=0, null=True, blank=True)
    kg1=models.BooleanField(default=False, blank=True, null=True)
    kg1_quan = models.IntegerField(default=0, null=True, blank=True)
    seller_details=models.ForeignKey(Seller, on_delete=models.CASCADE)
    img1=models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2=models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3=models.ImageField(upload_to='images/', default=None, blank=True, null=True)


    def __str__(self):
        return str(self.id) + " " + self.name


class Snacks(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    gm100 = models.BooleanField(default=None, blank=True, null=True)
    gm100_quan = models.IntegerField(default=0, blank=True, null=True)
    gm250 = models.BooleanField(default=None, blank=True, null=True)
    gm250_quan = models.IntegerField(default=0, blank=True, null=True)
    gm500 = models.BooleanField(default=None, blank=True, null=True)
    gm500_quan = models.IntegerField(default=0, blank=True, null=True)
    kg1 = models.BooleanField(default=None, blank=True, null=True)
    kg1_quan = models.IntegerField(default=0, blank=True, null=True)
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)

class Fruits(models.Model):
    name= models.CharField(max_length=50)
    quantity=models.IntegerField()
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    gm100=models.BooleanField(default=False, blank=True, null=True)
    gm100_quan = models.IntegerField(default=0, null=True, blank=True)
    gm250=models.BooleanField(default=False, blank=True, null=True)
    gm250_quan = models.IntegerField(default=0, null=True, blank=True)
    gm500=models.BooleanField(default=False, blank=True, null=True)
    gm500_quan = models.IntegerField(default=0, null=True, blank=True)
    kg1=models.BooleanField(default=False, blank=True, null=True)
    kg1_quan = models.IntegerField(default=0, null=True, blank=True)
    seller_details=models.ForeignKey(Seller, on_delete=models.CASCADE)
    img1=models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2=models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3=models.ImageField(upload_to='images/', default=None, blank=True, null=True)


    def __str__(self):
        return str(self.id) + " " + self.name


class Beverages(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField()
    l100 = models.BooleanField(default=None, blank=True, null=True)
    l100_quan = models.IntegerField(default=0, blank=True, null=True)
    l250 = models.BooleanField(default=None, blank=True, null=True)
    l250_quan = models.IntegerField(default=0, blank=True, null=True)
    l500 = models.BooleanField(default=None, blank=True, null=True)
    l500_quan = models.IntegerField(default=0, blank=True, null=True)
    l1 = models.BooleanField(default=None, blank=True, null=True)
    l1_quan = models.IntegerField(default=0, blank=True, null=True)
    l1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    seller_details = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.name


class KitchenCategory(models.Model):
    vegetables=models.ForeignKey(Vegetables, on_delete=models.CASCADE)
    fruits=models.ForeignKey(Fruits, on_delete=models.CASCADE)
    pulses=models.ForeignKey(Pulses, on_delete=models.CASCADE)
    frozen_foods=models.ForeignKey(FrozenFoods, on_delete=models.CASCADE)
    bakery=models.ForeignKey(Bakery, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + " " + self.name

