from django.shortcuts import render
from .models import *

def science_index(request):
    science = Science_Courses.objects.all()
    return render(request, 'science_courses/science_index.html', {'science': science})