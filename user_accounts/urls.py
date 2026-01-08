from user_accounts.views import signup,login_user
from django.urls import path

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('signin/',login_user,name='signin')
]

