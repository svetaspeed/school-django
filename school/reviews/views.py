from django.shortcuts import render
from .models import Rating


def reviews(request):
    obj = Rating.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, 'ratings/index.html', context)
