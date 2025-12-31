from django.shortcuts import render

# Create your views here.

def account_opening(request):
    return render(request,'users/account_opening.html')

