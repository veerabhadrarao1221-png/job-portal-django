from django.urls import path
from . import views

urlpatterns = [
    path('job/<int:job_id>/', views.view_applicants, name='view_applicants'),
    path('update/<int:application_id>/', views.update_status, name='update_status'),
]