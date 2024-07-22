from django.shortcuts import render
from .models import Blog
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm

def Home(request):
    Data = {'Blogs': Blog.objects.all().order_by('-date')}
    return render(request, 'home/home.html', Data)

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Điều hướng đến trang chính
    else:
        form = CustomAuthenticationForm()
    return render(request, 'home/login.html', {'form': form})
def blog(request):
    return render(request, 'home/home.html')



