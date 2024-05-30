from django.shortcuts import render
from .models import Blog


# Create your views here.
def blog(request):
    return render(request, 'home/home.html')

def list(request):
    Data = {'Blogs': Blog.objects.all().order_by('-date')}
    return render(request, 'home/home.html', Data)
