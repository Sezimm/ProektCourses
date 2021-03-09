from django.urls import path
from . import views


urlpatterns = [
    path('', views.science_index, name='science_home'),
]