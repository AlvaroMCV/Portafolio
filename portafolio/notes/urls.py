from django.urls import path
from . import views

urlpatterns = [
    path('mynotes/', views.my_notes, name='mynotes'),
    path('newnote/', views.new_note, name='newnote'),
    path('delete/<int:id>/', views.delete_note, name='deletenote'),
]