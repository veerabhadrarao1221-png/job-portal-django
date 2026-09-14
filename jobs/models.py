from django.db import models
from recruiters.models import Recruiter

class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('internship', 'Internship'),
        ('remote', 'Remote'),
    )

    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.TextField(help_text="Comma-separated skills, e.g. Python, Django, SQL")
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    salary_range = models.CharField(max_length=100, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.recruiter.company_name}"