from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'salary', 'posted_by', 'date_posted']
    search_fields = ['title', 'description']
    list_filter = ['date_posted', 'posted_by']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['job', 'applicant', 'date_applied']
    list_filter = ['date_applied', 'job']
    search_fields = ['applicant__username', 'job__title']
