from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
    phone = forms.CharField(max_length=15, required=False)

    # Recruiter-only field
    company_name = forms.CharField(max_length=200, required=False)

    # Job Seeker-only fields
    skills = forms.CharField(widget=forms.Textarea, required=False)
    experience_years = forms.IntegerField(required=False, min_value=0)
    location = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'phone']