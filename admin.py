from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'category', 'created_at']
    search_fields = ['title', 'location', 'category']
    list_filter = ['location', 'category']
    list_display_links = ['title']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'applied_for', 'applied_on']
    list_display_links = ['name', 'applied_for']
    search_fields = ['name', 'email', 'applied_for__title']
    list_filter = ['applied_on']
    readonly_fields = ['applied_on']
