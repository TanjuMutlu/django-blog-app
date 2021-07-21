from django import forms
from django.shortcuts import render,redirect
from .forms import registerForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

def register(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,"Basariyla Kayit Oldunuz")
            
            return redirect("index")
            
        form = registerForm()
        context = {"form":form }
        return render(request,"register.html",context)


    else:
        form = registerForm()
        context = {"form":form }
        return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {"form":form }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanici adi veya parola hatali")
            return render(request,"login.html",context)
            
        messages.success(request,"Basariyla Giris Yaptiniz")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)

    
def logoutUser(request):
    logout(request)
    messages.success(request,"Cikis Yaptiniz")
    return redirect("index")