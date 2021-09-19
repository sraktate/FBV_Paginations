from django.urls import path
from .views import Home_view,Laptop_add_view,Laptop_show_view

urlpatterns=[
    path('home/',Home_view,name='home'),
    path('laptopadd/',Laptop_add_view,name='laptopadd'),
    path('laptopshow/',Laptop_show_view,name='laptopshow'),
]