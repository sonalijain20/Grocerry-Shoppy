from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=20)
    #lname = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email = models.EmailField(default=None, null=True, blank=True)
    phone = models.CharField(max_length=20, default=None, null=True, blank=True)
    address1 = models.CharField(max_length=20, default=None, null=True, blank=True)
    landmark = models.CharField(max_length=20, default=None, null=True, blank=True)
    city = models.CharField(max_length=20, default=None, null=True, blank=True)
    state = models.CharField(max_length=20 ,default=None, null=True, blank=True)
    pin = models.CharField(max_length=20 ,default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.name
