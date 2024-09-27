from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='Homepage'),
    path('create_submission/', views.create_submission, name='create_submission'),
    path('faculty_files/', views.faculty_files, name='faculty_files'),
    path('my_profile/', views.my_profile, name='My_profile'),
]