from django.shortcuts import render, redirect
from .models import *

# Create your views here.

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
    context = {'recipes': queryset}

    return render(request, "recipes.html", context)

def delete_recipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipe')
