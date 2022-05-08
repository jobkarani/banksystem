from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render (request, "all-temps/index.html")

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "all-temps/profile.html", {"profile": profile})

@login_required(login_url="/accounts/login/")
def createBankAccount(request):
    current_user = request.user
    account = BankAccount.objects.all()
    return render (request, "all-temps/createaccount.html", {"account":account})

@login_required(login_url="/accounts/login/")
def deposit(request):
    current_user = request.user
    to = BankAccount.objects.all()
    return render (request, "all-temps/deposit.html", {"to":to})

@login_required(login_url="/accounts/login/")
def withdraw(request):
    current_user = request.user
    fromm = BankAccount.objects.all()
    return render (request, "all-temps/withdraw.html", {"fromm":fromm})

@login_required(login_url="/accounts/login/")
def transfer(request):
    current_user = request.user
    fromm = BankAccount.objects.all()
    to = BankAccount.objects.all()
    return render (request, "all-temps/transfer.html", {"fromm":fromm, "to":to})

@login_required(login_url="/accounts/login/")
def checkBalance(request):
    current_user = request.user
    account = BankAccount.objects.all()
    return render (request, "all-temps/checkBalance.html", {"account":account})
