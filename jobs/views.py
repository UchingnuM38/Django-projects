from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Job, Application
from .forms import JobForm


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'all_jobs'
    paginate_by = 10


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['applied'] = Application.objects.filter(
                job=self.object, applicant=self.request.user
            ).exists()
        return context


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job-list')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        messages.success(self.request, 'Job posted successfully!')
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('job-list')

    def test_func(self):
        job = self.get_object()
        return self.request.user == job.posted_by

    def handle_no_permission(self):
        messages.error(self.request, 'You can only edit your own jobs!')
        return redirect('job-list')

    def form_valid(self, form):
        messages.success(self.request, 'Job updated successfully!')
        return super().form_valid(form)


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job-list')

    def test_func(self):
        job = self.get_object()
        return self.request.user == job.posted_by

    def handle_no_permission(self):
        messages.error(self.request, 'You can only delete your own jobs!')
        return redirect('job-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Job deleted successfully!')
        return super().delete(request, *args, **kwargs)


class MyJobsListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/my_jobs_list.html'
    context_object_name = 'my_jobs'
    paginate_by = 10

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user).order_by('-date_posted')


class MyApplicationsListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'jobs/my_applications_list.html'
    context_object_name = 'my_applications'
    paginate_by = 10

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).select_related('job', 'applicant').order_by('-date_applied')


@login_required(login_url='login')
def apply_to_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    # Check if already applied
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.warning(request, 'You have already applied to this job!')
        return redirect('job-detail', pk=pk)
    
    # Create application
    application = Application.objects.create(
        job=job,
        applicant=request.user
    )
    
    messages.success(request, 'Application submitted successfully!')
    return redirect('job-detail', pk=pk)