from django.shortcuts import render
from .models import *

def lang_index(request):
    lang = Lang_Courses.objects.all()
    return render(request, 'lang_courses/lang_index.html', {'lang':lang})
