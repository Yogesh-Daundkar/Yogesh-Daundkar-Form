from django.shortcuts import render,redirect
from .models import *

# Create your views
def home(request):
    return render(request, 'Formapp/main.html')

def process(request):
    

    Candidate.objects.create(

    name = request.POST['name'],
    email = request.POST['email'],
    password = request.POST['password']
    )
    return redirect(home)

def list_view (request):
    context = {}
    context["dataset"] = Candidate.objects.all()
    return render(request, "Formapp/list_view.html", context)