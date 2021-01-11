from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, Group

group = Group(name = "Editor")

from .models import GEO_TAGGING

# Create your views here.

def form(request):
    return render(request,'dbms/form.html')

def logout(request):
    logout(request)
    return redirect("/")

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username ,password = password)
            login(request,user)
            return redirect('cityform')
    else:
        form = UserCreationForm()
    context = { 'form' : form }
    return render(request,'registration/registration.html',context)

def CityForm(request):
    if request.method=="POST":
        district = request.POST['district']
        city = request.POST['city']
        dpr_no = request.POST['dpr_no']
        balance = request.POST['balance']
        date = request.POST['date']
        G=GEO_TAGGING(district = district , city = city , dpr_no = dpr_no,balance = balance , date =date)
        G.user=request.user
        G.save()
        return redirect('cityform')
    return render(request,'dbms/cityform.html')

def All_People(request):
    if request.method == 'GET': 
        users_in_group = Group.objects.get(name="Admin").user_set.all()
        # print(users_in_group)
        # print(request.user)
        if request.user in users_in_group:
            users = GEO_TAGGING.objects.all()
        else:
            users = {}
        return render(request, 'dbms/table.html', {'users' : users})

def Fund_Form(request):
    return render(request, 'dbms/fund.html')
