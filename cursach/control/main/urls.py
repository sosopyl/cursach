from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('notify/', views.notify, name='notify'),
    path('lessons/', views.lessons, name='lessons'),
    path('classes/', views.classes, name='classes'),
    path('checking/', views.checkin, name='checking'),
]
