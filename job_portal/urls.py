from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('jobseekers/', include('jobseekers.urls')),
    path('recruiters/', include('recruiters.urls')),
    path('jobs/', include('jobs.urls')),
    path('applications/', include('applications.urls')),
]