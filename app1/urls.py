from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('blog/',views.blog),
    path('service/',views.service)


]
