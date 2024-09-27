from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model



#creating a Profile model that will serve as a link to existing user model and includes references to the department and role models
class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)

  

  FACULTY = 'faculty' 
  PC ='pc'

  ROLE_CHOICES = [
    (FACULTY, 'Faculty'),
    (PC, 'PC')
  ]

  CICT= 'cict'
  BME = 'bme'

  DEPARTMENT_CHOICES = [
    (CICT, 'CICT'),
    (BME, 'BME')
  ]


  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=FACULTY)
  department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES, default=CICT)


def __str__(self):
    return f"{self.user.username} - {self.get_role_display()} - {self.get_department_display()}"
  


