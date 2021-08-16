from django.urls import path
from .views import reviews, rate_reviews

urlpatterns = [
    path('reviews', reviews, name='reviews'),
    path('rate/', rate_reviews, name='rate')
]
