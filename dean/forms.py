from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = [
        ('faculty', 'Faculty'),
        ('pc', 'PC')
    ]

    DEPARTMENT_CHOICES = [
        ('cict', 'CICT'),
        ('bme', 'BME')
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'department', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                role=self.cleaned_data['role'],
                department=self.cleaned_data['department']
            )
        return user
