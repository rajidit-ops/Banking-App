from user_accounts.views import signup,login
from django.urls import path

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('signin/',login,name='signin')
]

