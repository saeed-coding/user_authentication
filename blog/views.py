from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def home(request):
#     return HttpResponse("""
#     <h1>I am a server</h1>
#     <p>Here is paragraph </p>
#     <hr>
#     <h3> here is h3</h3>
#     """)
def home(request):
    dummy_data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 32},
        {"name": "Charlie", "age": 29},
        {"name": "Diana", "age": 24},
        {"name": "Ethan", "age": 31},
        {"name": "Fiona", "age": 27},
        {"name": "George", "age": 35},
        {"name": "Hannah", "age": 22},
        {"name": "Ian", "age": 30},
        {"name": "Julia", "age": 28}
    ]

    return render(request, 'home/index.html', context={'people': dummy_data})

def about_page(request):
    return render(request, 'home/about.html')

def contact_page(request):
    return render(request, 'home/contact.html')

def success_page(request):
    return render(request, 'login_success.html')
