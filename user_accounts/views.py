from django.shortcuts import render,redirect
from user_accounts.models import UserAccounts
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate,login 
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("psw")
        confirm_password = request.POST.get("psw-repeat")
        print(fname,lname,email,password,confirm_password)

        if password != confirm_password:
            return render(request,'user_accounts/signup.html',{
                "error":"Password and Confirm password do not match"
            })

        if UserAccounts.objects.filter(email=email).exists():
            return render(request,'user_accounts/signup.html',{
                "error":"User with this email already exists"
            })


        UserAccounts.objects.create_user(
            first_name = fname,
            last_name = lname,
            email = email,
            password = password,

        )

        send_mail(
            subject = "Welcome to My Bank",
            message= f"Hi {fname}, welcome to my bank. your username setup is successfull",
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list= {email}
        )
        return render(request,'user_accounts/signin.html')
    return render(request,'user_accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = UserAccounts.objects.get(email=email)

            if user.password == password:
                request.session["user_email"] = user.email
                request.session["user_name"] = user.first_name
                messages.success(request, "Login successful")
                return redirect("/")
            else:
                messages.error(request, "Invalid password")
        except UserAccounts.DoesNotExist:
            messages.error(request, "User does not exist")

    return render(request, "user_accounts/signin.html")