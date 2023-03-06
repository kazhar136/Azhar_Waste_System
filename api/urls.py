from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('waste/', WasteAPIView.as_view()),
    path('register/', RegisterUser.as_view()),
   
]