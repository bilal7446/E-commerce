
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index,name="shopHome"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contactUs"),
    path('tracker/', views.tracker,name="trakingstatus"),
    path('search/', views.search,name="search"),
    path('products/<int:myid>', views.prodView,name="productinfo"),
    path('checkout/', views.checkout,name="checkouts"),
]
