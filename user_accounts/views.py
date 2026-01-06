from django.shortcuts import render
from user_accounts.models import UserAccounts

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


        UserAccounts.objects.create(
            first_name = fname,
            last_name = lname,
            email = email,
            password = password,

        )

        return render(request,'user_accounts/signup.html')
    return render(request,'user_accounts/signup.html')
