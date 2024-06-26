from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('onbuild/', views.on_build, name='onbuild'),
    path('aboutme/', views.about_me, name='aboutme'),
]