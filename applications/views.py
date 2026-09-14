from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Application
from jobs.models import Job
from recruiters.models import Recruiter


@login_required
def view_applicants(request, job_id):
    recruiter = Recruiter.objects.get(profile__user=request.user)
    job = get_object_or_404(Job, id=job_id, recruiter=recruiter)
    applications = job.applications.all()

    return render(request, 'applications/view_applicants.html', {
        'job': job,
        'applications': applications
    })


@login_required
def update_status(request, application_id):
    recruiter = Recruiter.objects.get(profile__user=request.user)
    application = get_object_or_404(Application, id=application_id, job__recruiter=recruiter)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['applied', 'shortlisted', 'rejected', 'hired']:
            application.status = new_status
            application.save()

    return redirect('view_applicants', job_id=application.job.id)