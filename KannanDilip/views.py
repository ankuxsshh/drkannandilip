from django.http import HttpResponse
from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def expertise_view(request):
    return render(request, 'achievements.html')

def articles_view(request):
    return render(request, 'articles.html')

def contact_view(request):
    return render(request, 'contact.html')

