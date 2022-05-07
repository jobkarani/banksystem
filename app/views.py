from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "all-temps/profile.html", {"profile": profile})

@login_required(login_url="/accounts/login/")
def deposit(request):
    current_user = request.user
    to = BankAccount.objects.all()
    return render (request, "all-temps/deposit.html", {"to":to})