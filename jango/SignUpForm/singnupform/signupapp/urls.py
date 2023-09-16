# appname/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    # Add other URL patterns for your app here
]
