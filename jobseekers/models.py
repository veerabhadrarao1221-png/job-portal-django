from django.db import models
from accounts.models import Profile

class JobSeeker(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(blank=True, help_text="Comma-separated skills, e.g. Python, Django, SQL")
    experience_years = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.profile.user.username