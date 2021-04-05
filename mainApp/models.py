from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    #lname = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20, default=None, null=True, blank=True)
    address1 = models.CharField(
        max_length=20, default=None, null=True, blank=True)
    landmark = models.CharField(
        max_length=20, default=None, null=True, blank=True)
    city = models.CharField(max_length=20, default=None, null=True, blank=True)
    state = models.CharField(
        max_length=20, default=None, null=True, blank=True)
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
    img1 = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
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
    img1 = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
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
    img1 = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
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
