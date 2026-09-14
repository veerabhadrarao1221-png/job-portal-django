from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
    path('my-applications/', views.my_applications, name='my_applications'),
]