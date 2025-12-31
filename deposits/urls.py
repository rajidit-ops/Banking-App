from .views import display
from django.urls import path

urlpatterns = [
    path('',display,name='welcome')
]
