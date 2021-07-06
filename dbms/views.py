from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, Group
from .forms import SignUpForm,Form


group = Group(name = "Editor")

from .models import Student,Img,Videos,Enroll

# Create your views here.

def form(request):
    
    return render(request,'dbms/form.html')

def adminhome(request):
    if request.user.is_staff != True:
        request.user.is_staff = True
    return render(request,'dbms/adminhome.html')

def allcourse(request):
    Plants = Img.objects.all()
    return render(request,'dbms/classes/allcourse.html',{'plant_images' : Plants})

def tests(request):
    return render(request,'dbms/tests/tests.html')

def uploadcourse(request):
    if request.method=="POST":
        animal = Img(user=request.user)  
        form =Form(request.POST, request.FILES,instance=animal)
        if form.is_valid():
            animal.save()
            return redirect('allcourse')
        else:
            print(form.errors)

    return render(request,'dbms/UploadCourses/uploadcourses.html')

def uploadcoursecontent(request):
    if request.method == 'POST': 
         
        title = request.POST['title']
        video = request.FILES['video']
        name = request.POST['cousrename']
        description = request.POST['description']
         
        content = Videos(title=title,video=video,description=description)
        content.user= Img.objects.get(coursename=name)
        content.save()
        return redirect('cityform')

    return render(request,'dbms/UploadCourses/uploadcoursecontent.html')

    
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

def adminregister(request):
    if request.method=="POST":
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username ,password = password)
            login(request,user)
            return render(request,'registration/adminhome.html')
    else:
        form = UserCreationForm()
    context = { 'form' : form }
    return render(request,'registration/adminregister.html')

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


def detail(request, id):
    product=Img.objects.get(id=id)
    
    if request.method=="POST":
        G=Enroll()
        G.user=request.user
        G.img=product
        G.save()
        return redirect('enroll')
    try:
        G = Enroll.objects.get(img=product,user=request.user)
        #print(G)
        if G.id!=None:
            a=1
        else:
            a=0
        #print(a)
        context={'product':product,'enroll':a}
        return render(request,"dbms/Detail/detail.html",context)
    except:
        pass
    
    
    
    context={'product':product}
    return render(request,"dbms/Detail/detail.html",context)

def coursedetail(request, id):
    product=Img.objects.get(id=id)
    
    videos = Videos.objects.all()
    context={'product':product ,'videos':videos}
    print(videos)
    

    return render(request,"dbms/Detail/content.html",context)

def videocontent(request, id):
    videos=Videos.objects.get(id=id)
    context={'videos':videos}
    

    return render(request,"dbms/Detail/video.html",context)

def enrollcourse(request):
    enrolled = Enroll.objects.all().filter(user=request.user)
    # for i in enrolled:
    #     print(i.user.username)
    context = {'enroll' : enrolled}
    return render(request,"dbms/enroll/enroll.html",context)

