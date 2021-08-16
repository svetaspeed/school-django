from django.shortcuts import render
from .models import Rating
from django.http import JsonResponse


def reviews(request):
    obj = Rating.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, 'ratings/index.html', context)

def rate_reviews(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        obj = Rating.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success': 'true', 'score': val}, safe=False)
    return JsonResponse({'success': 'false'})
