from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('predict/', views.extract_validate, name="predict"),
    path('redirect/',views.redirect, name="redirect"),
    path('github/', views.github, name="github"),
    path('linkedin/', views.linkedin, name="linkedin"),
]