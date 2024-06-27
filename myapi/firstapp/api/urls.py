from django.urls import path
from .views import firstfunction

urlpatterns = [
    path('first/', firstfunction),  # Include trailing slash for consistency
]