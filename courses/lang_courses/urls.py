from django.urls import path
from . import views


urlpatterns = [
    path('', views.lang_index, name='lang_home'),
]