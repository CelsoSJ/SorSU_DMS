from django.shortcuts import render

# Create your views here.
def homepage(request):
  return render(request, 'pc/Home.html')


def create_submission(request):
  return render(request, 'pc/Create_Submission.html')

def faculty_files(request):
  return render(request, 'pc/Faculty_Files.html')

def my_profile(request):
  return render(request, 'pc/My_Profile.html')
