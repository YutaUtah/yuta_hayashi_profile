from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='main'),
	path('dog/', views.dog_pics),
	path('index/', views.index),
]