from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recruiter


@login_required
def recruiter_dashboard(request):
    recruiter = Recruiter.objects.get(profile__user=request.user)
    jobs = recruiter.jobs.all()
    return render(request, 'recruiters/dashboard.html', {'jobs': jobs})