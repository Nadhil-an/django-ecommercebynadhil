from django.urls import path
from .views import home

urlpatterns = [
    path('store/', home, name='home'),
]
