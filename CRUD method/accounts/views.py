from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Testmodel, formmodel
from accounts.forms import BannerForm

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello</h1>")

def dashboard(request):
    return render(request,'dash.html')

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("done")
        else:
            return HttpResponse("formnot valid")
    else:
        form = UserCreationForm()
        return render(request,'reg.html',{'form':form})

def upload(request):
    if request.method == "POST":
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dash')
    else:
      form = BannerForm()
      return render(request,'upload.html',{'form':form})


def contact(request):
    if(request.method=='GET' and request.GET.get('method')=='delete' and request.GET.get('id')):
        name = formmodel.objects.filter(id=request.GET.get('id'))
        name.delete()
    if(request.method=='GET' and request.GET.get('method')=='edit' and request.GET.get('id')):
        name = formmodel.objects.filter(id=request.GET.get('id')).get()
        return render(request,'edit.html',{'name':name})
    if request.method=='POST':
        if request.GET.get('method')=='edit':
            name = formmodel.objects.filter(id=request.GET.get('id'))
            name.update(
                fname = request.POST['fname'],
                lname = request.POST['lname']
            )
            return redirect('/contact')
        else:
            a = request.POST.get('fname')
            b = request.POST.get('lname')
            c = formmodel(fname=a,lname=b)
            c.save()
            return redirect('/contact')

    names = formmodel.objects.all()
    return render(request,'contact.html',{'names':names})
