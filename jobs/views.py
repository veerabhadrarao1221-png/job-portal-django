from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .models import Job
from recruiters.models import Recruiter
from jobseekers.models import JobSeeker
from applications.models import Application


@login_required
def post_job(request):
    recruiter = Recruiter.objects.get(profile__user=request.user)

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = recruiter
            job.save()
            return redirect('recruiter_dashboard')
    else:
        form = JobForm()

    return render(request, 'jobs/post_job.html', {'form': form})


@login_required
def job_list(request):
    jobs = Job.objects.filter(is_active=True).order_by('-posted_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


@login_required
def apply_to_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    jobseeker = JobSeeker.objects.get(profile__user=request.user)

    Application.objects.get_or_create(job=job, jobseeker=jobseeker)

    return redirect('job_list')

from django.http import JsonResponse

@login_required
def search_jobs(request):
    query = request.GET.get('q', '')
    jobs = Job.objects.filter(is_active=True)

    if query:
        jobs = jobs.filter(title__icontains=query) | jobs.filter(required_skills__icontains=query) | jobs.filter(location__icontains=query)

    results = []
    for job in jobs:
        results.append({
            'id': job.id,
            'title': job.title,
            'company': job.recruiter.company_name,
            'location': job.location,
            'job_type': job.job_type,
            'skills': job.required_skills,
            'description': job.description,
        })

    return JsonResponse({'jobs': results})