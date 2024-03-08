
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),

    path('clear/', views.clear, name='delete')

]
