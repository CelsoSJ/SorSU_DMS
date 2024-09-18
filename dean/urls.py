from django.urls import path
from . import views
from .views import test_db_connection

urlpatterns = [
    path('homepage/', views.home_page, name='home_page'),
    path('files/', views.files, name='files'),
    path('archive/', views.archive, name='archive'),
    path('myprofile/', views.my_profile, name='my_profile'),
    path('userManagement/', views.userManagement, name='userManagement'),
    path('test-db/', test_db_connection),
]