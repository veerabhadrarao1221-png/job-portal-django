from django.db import models
from accounts.models import Profile

class Recruiter(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_website = models.URLField(blank=True)

    def __str__(self):
        return self.company_name