from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_recipe(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if not user.exists():
            messages.info(request, "Invalid Username")
            return redirect("/login_recipe/")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/recipe/")
        else:
            messages.info(request, "Invalid Password")
            return redirect("/login_recipe/")

    return render(request, "login.html")

def register_recipe(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.POST.get('username'))
        if user.exists():
            messages.info(request, "Username already Exists")
            return redirect("/register_recipe/")
        user = User.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            username=request.POST.get('username'),
            email=request.POST.get('email'),
        )
        user.set_password(request.POST.get('password'))
        user.save()
        messages.info(request, "Account Created Successfully")
        return redirect("/register_recipe/")

    return render(request, "register.html")

def logout_recipe(request):
    logout(request)
    return redirect("/login_recipe/")

@login_required(login_url="/login_recipe/")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        Receipe.objects.create(
            name=name,
            description=description,
            image=image,
        )
        return redirect("/recipe")
    queryset = Receipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))
    
    context = {'recipes': queryset}
    return render(request, "recipes.html", context)

@login_required(login_url="/login_recipe/")
def delete_recipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipe')

@login_required(login_url="/login_recipe/")
def update_recipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')
        queryset.name = name
        queryset.description = description

        if image:
            queryset.image = image

        queryset.save()
        return redirect('/recipe')

    context = {'recipe': queryset}
    return render(request, "update_recipes.html", context)


