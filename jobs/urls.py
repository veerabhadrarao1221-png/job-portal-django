from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_job, name='post_job'),
    path('', views.job_list, name='job_list'),
    path('apply/<int:job_id>/', views.apply_to_job, name='apply_to_job'),
    path('search/', views.search_jobs, name='search_jobs'),
]