from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Subject, Mark ,Student,Math,Test,Physics,Chem
from AddSubject.forms import MarkForm,StudForm ,MathForm,PhyForm,ChemForm,TestForm,SimpForm
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello</h1>")

def addsub(request):
    if request.method == 'POST':
        a = request.POST.get('subname')
        b = request.POST.get('subcode')
        c = request.POST.get('maxmarks')
        d = request.POST.get('coursename')
        e = request.POST.get('branchname')
        f = request.POST.get('sem')

        abc = Subject(Subject_Name = a, Subject_Code = b, Max_Marks = c, Course = d, Branch = e, Semester = f)
        abc.save()
        return redirect('addsub')
    else:
        return render(request, 'AddSubject.html')


def addstud(request):
    if request.method == 'POST':
        form = StudForm(request.POST)
        print('user created')
        if form.is_valid():
            form.save()
            a = request.POST.get('studname')
            b = request.POST.get('dob')
            user = User.objects.create_user(username=a,password=b)
            user.save()
            messages.add_message(request, messages.INFO, 'Student successfully registered. Add more !')
            return redirect('/addstud')
        else:
            messages.add_message(request, messages.INFO, 'Please enter correct fields.')
            return redirect('/addstud')
    else:
        form = StudForm()
        return render(request, 'addstud.html',{'form':form})

def search(request):
    if request.method=='POST':
        a = request.POST.get('studroll')
        std = Student.objects.get(studroll=a)
        form = MarkForm()
        messages.add_message(request, messages.INFO, 'Please enter student marks')
        return render(request,'AddMark2.html',{'std':std,'form':form})
    else:
        return render(request,'search.html')

def addmark(request):
    if request.method == 'POST':
        a = request.POST.get('roll')
        b = request.POST.get('subcode')
        if a is not None:
            if b=='mmb':
                form = MathForm(request.POST,request.FILES)
                post = form.save(commit=False)
                post.roll = a
                post.save()
            if b=='ppb':
                form = PhyForm(request.POST,request.FILES)
                post = form.save(commit=False)
                post.roll = a
                post.save()
            if b=='ccb':
                form = ChemForm(request.POST,request.FILES)
                post = form.save(commit=False)
                post.roll = a
                post.save()
            messages.add_message(request, messages.INFO, 'Marks added successfully. Search again')
            return redirect('/search')
        else:
            return HttpResponse('ERROR SAVING')
    else:
        return redirect('/search')

def upload(request):
    if request.method == 'POST':
        a = request.POST.get('cont')
        form = SimpForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.country = a
            post.save()
            return HttpResponse('saved')
        else:
            return HttpResponse('ERROR SAVING')
    else:
        form = SimpForm()
        return render(request,'upload.html',{'form':form})
        