from django.db import models
from jobs.models import Job
from jobseekers.models import JobSeeker

class Application(models.Model):
    STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired'),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'jobseeker')

    def __str__(self):
        return f"{self.jobseeker.profile.user.username} → {self.job.title}"