from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Subject, Mark ,Student
from AddSubject.forms import MarkForm

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
        a = request.POST.get('studname')
        b = request.POST.get('studroll')
        c = request.POST.get('coursename')
        d = request.POST.get('branchname')
        e = request.POST.get('sem')

        xyz = Student(studname=a,studroll=b,coursename=c,branchname=d,sem=e)
        xyz.save()
        return redirect('addstud')
    else:
        return render(request, 'addstud.html')

def search(request):
    if request.method=='POST':
        a = request.POST.get('studroll')
        std = Student.objects.get(studroll=a)
        form = MarkForm()
        return render(request,'AddMark.html',{'std':std,'form':form})
    else:
        return render(request,'search.html')

def addmark(request):
    if request.method == 'POST':
        form = MarkForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/addmark')
    else:
        form = MarkForm()
        return render(request,'AddMark.html',{'form':form})
