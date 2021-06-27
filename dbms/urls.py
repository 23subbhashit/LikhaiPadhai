from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.form,name="cityform"),
    path('chatbot',views.chatbot,name="chatbot"),
    path('allcourse',views.allcourse,name="allcourse"),
    path('tests',views.tests,name="tests"),
    path('<int:id>/detail/',views.detail,name='detail'),
    path('upload',views.uploadcourse,name='upload'),
    path('city',views.StudentForm,name="city"),
    path('register',views.register,name='register'),
    path('logout', views.logout, name = 'logout'),
    path('users', views.All_People, name = 'users'),
    path('reset_password',
    auth_views.PasswordResetView.as_view(template_name="dbms/password_reset_form.html"),name="rp"),

    path('accounts/password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name="dbms/password_reset_done.html"),name="rps"),

    path('accounts/reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="dbms/password_reset_confirm.html"),name="r"),

    path('accounts/reset/done/',
    auth_views.PasswordResetView.as_view(template_name="dbms/password_reset_complete.html"),name="rpc"),


]