from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.order_by('-id')[:1]
    return render(request, 'index.html', {'title': 'Главная cтраница', 'news': news})

def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')

def specialties(request):
    return render(request, 'specialties.html')
