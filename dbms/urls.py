from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.form,name="cityform"),
    #Register
    path('city',views.CityForm,name="city"),
    path('register',views.register,name='register'),
    path('logout', views.logout, name = 'logout'),
    path('users', views.All_People, name = 'users')

]