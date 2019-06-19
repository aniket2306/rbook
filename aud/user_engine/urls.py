from django.urls import path, include
from core import views 

urlpatterns = [
    path('<str:username>/',views.home),
]
