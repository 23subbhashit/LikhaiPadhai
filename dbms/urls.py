from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.form,name="cityform"),
    path('home',views.form1,name="cityform1"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('adminregister',views.adminregister,name="adminregister"),
    path('chatbot',views.chatbot,name="chatbot"),
    path('allcourse',views.allcourse,name="allcourse"),
    path('uploadcontent',views.uploadcoursecontent,name="uploadcontent"),
    path('uploadquizcontent',views.uploadquizcontent,name="uploadquizcontent"),
    path('profile',views.userprofile,name="profile"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('enroll',views.enrollcourse,name="enroll"),
    path('tests',views.tests,name="tests"),
    path('exams',views.allexams,name="exams"),
    path('<int:id>/detail/',views.detail,name='detail'),
    path('<int:id>/examdetail/',views.examdetail,name='examdetail'),
    path('<int:id>/content/',views.coursedetail,name='coursedetail'),
    path('<int:id>/quizcontent/',views.quizdetail,name='quizdetail'),
    path('<int:id>/quizresult/',views.quizresult,name='quizresult'),
    path('<int:id>/video/',views.videocontent,name='video'),
    path('upload',views.uploadcourse,name='upload'),
    path('uploadexam',views.uploadexam,name='uploadexam'),
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