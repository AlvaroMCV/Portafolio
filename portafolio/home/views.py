from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def on_build(request):
    return render(request, 'common/on_build.html')

def about_me(request):
    return render(request, 'home/about_me.html')