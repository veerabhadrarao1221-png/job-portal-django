from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import JobSeeker


@login_required
def jobseeker_dashboard(request):
    return render(request, 'jobseekers/dashboard.html')


@login_required
def my_applications(request):
    jobseeker = JobSeeker.objects.get(profile__user=request.user)
    applications = jobseeker.applications.all()
    return render(request, 'jobseekers/my_applications.html', {'applications': applications})