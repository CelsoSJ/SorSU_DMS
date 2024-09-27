from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm



# user log in 

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
        
        login(request, user)
        if user.groups.filter(name='Dean').exists():
          return redirect('home_page')
        elif user.profile.role == 'pc':
          return redirect('Homepage')
        elif user.groups.filter(name='Quality_Assurance_Officer').exists():
          return redirect('homePage')
        elif user.profile.role == 'faculty':
          return redirect('homepage')
      
      else:
        form.add_error(None, 'Invalid username or  password')

  else:
    form = LoginForm()


  return render(request, 'login/Login.html', {'form':form})          





#creating a function logout
def log_out(request):
  logout(request)
  return redirect('login')