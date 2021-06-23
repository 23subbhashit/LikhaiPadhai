from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, Group
from .forms import SignUpForm

group = Group(name = "Editor")

from .models import Student

# Create your views here.

def form(request):
    return render(request,'dbms/form.html')

def allcourse(request):
    return render(request,'dbms/classes/allcourse.html')

def tests(request):
    return render(request,'dbms/tests/tests.html')

def uploadcourse(request):
    return render(request,'dbms/UploadCourses/uploadcourses.html')


    
def chatbot(request):
    return render(request,'dbms/index.html')

def logout(request):
    logout(request)
    return redirect("/")

def register(request):
    if request.method=="POST":
        
        form =SignUpForm(request.POST)
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

def StudentForm(request):
    if request.method=="POST":
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        usn = request.POST['usn']
        G=Student(name = name , phonenumber = phonenumber , address =address,usn = usn)
        G.user=request.user
        G.save()
        return redirect('cityform')
    return render(request,'dbms/cityform.html')

def All_People(request):
    if request.method == 'GET': 
        users_in_group = Group.objects.get(name="Admin").user_set.all()
        if request.user in users_in_group:
            users = Student.objects.all()
        else:
            users = {}
        return render(request, 'dbms/table.html', {'users' : users})

def Fund_Form(request):
    return render(request, 'dbms/fund.html')
