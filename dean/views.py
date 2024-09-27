from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Profile


# Create your views here.


def home_page(request):
  return render(request,'dean/home.html')



def files(request):
  return render(request,'dean/files.html')


def archive(request):
  return render(request,'dean/archive.html')


def my_profile(request):
  return render(request,'dean/myprofile.html')



def userManagement(request):
  profiles = Profile.objects.all()
  return render(request,'dean/userManagement.html', {'profiles':profiles})



def test_db_connection(request):
  try:
    with connection.cursor() as cursor:
      cursor.execute("SELECT 1")
    return HttpResponse("Database connection successful!")
  except Exception as e:
    return HttpResponse(f"Database connection failed: {e}")




#user creation

def create_user(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user= form.save()

      if not Profile.objects.filter(user=user).exists():
                Profile.objects.create(
                    user=user,
                    role=form.cleaned_data['role'],
                    department=form.cleaned_data['department']
                )
    
      return redirect('userManagement')
    
  else:
    form = CustomUserCreationForm() 
  

  return render(request, 'dean/create_user.html', {'form':form})   



