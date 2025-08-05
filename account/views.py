from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    def get(self, request):
        return render(request, 'account/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'account/register.html', {'error': 'User already exists'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    

class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student-list')
        return render(request, 'account/login.html', {'error': 'Invalid credentials'})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')
