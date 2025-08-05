from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
import json
from django.shortcuts import render, redirect
from django.contrib import messages


class HomeView(View):
    def get(self, request):
        return render(request, 'middlewareproj/home.html')
    
class LoginPageView(View):
    def get(self, request):
        return render(request, 'middlewareproj/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect('home')

        messages.error(request, "Invalid email or password.")
        return redirect('login_page')


class LogoutPageView(View):
    def get(self, request):
        logout(request)
        return redirect('login_page')     
  