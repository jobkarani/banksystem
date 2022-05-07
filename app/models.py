from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    account_number = models.IntegerField(null=False)
    amount = models.IntegerField(null=True)
    date_created     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account_number

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)
    deposit = models.IntegerField(null=True)
    withdraw = models.IntegerField(null=True)
    transfer = models.IntegerField(null=True)

    def __str__(self):
        return self.user

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_photo = CloudinaryField('image')
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)
    account = models.ForeignKey(BankAccount, on_delete=models.PROTECT)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return self.phone

    def __str__(self):
        return self.user.username