from django.urls import path
from . import views

urlpatterns = [
    path('mynotes/', views.my_notes, name='mynotes'),
    path('newnote/', views.new_note, name='newnote'),
    path('oncontruction/', views.on_contruction, name='oncontruction'),
]