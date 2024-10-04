from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index/', index),
    path('start_football', index)
]