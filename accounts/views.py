from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Profile
from recruiters.models import Recruiter
from jobseekers.models import JobSeeker


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']

            profile = Profile.objects.create(
                user=user,
                role=role,
                phone=form.cleaned_data['phone']
            )

            if role == 'recruiter':
                Recruiter.objects.create(
                    profile=profile,
                    company_name=form.cleaned_data['company_name'] or 'Unnamed Company'
                )
            elif role == 'jobseeker':
                JobSeeker.objects.create(
                    profile=profile,
                    skills=form.cleaned_data['skills'],
                    experience_years=form.cleaned_data['experience_years'] or 0,
                    location=form.cleaned_data['location']
                )

            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def home(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('/admin/')  # superuser or any user without a profile

    if profile.role == 'jobseeker':
        return redirect('jobseeker_dashboard')
    elif profile.role == 'recruiter':
        return redirect('recruiter_dashboard')
    elif profile.role == 'admin':
        return redirect('/admin/')

    return render(request, 'accounts/home.html')