from django.urls import path
from . import views

urlpatterns = [
    # Job List and Detail
    path('', views.JobListView.as_view(), name='job-list'),
    path('job/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
    
    # Job Create, Update, Delete
    path('job/create/', views.JobCreateView.as_view(), name='job-create'),
    path('job/<int:pk>/update/', views.JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', views.JobDeleteView.as_view(), name='job-delete'),
    
    # My Jobs and Applications
    path('my-jobs/', views.MyJobsListView.as_view(), name='my-jobs'),
    path('my-applications/', views.MyApplicationsListView.as_view(), name='my-applications'),
    
    # Apply to Job
    path('job/<int:pk>/apply/', views.apply_to_job, name='apply-job'),
]
