from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'IT_courses/index.html')

def itindex(request):
    prog = Prog_Lang.objects.all()
    return render(request, 'IT_courses/itindex.html', {'prog': prog})