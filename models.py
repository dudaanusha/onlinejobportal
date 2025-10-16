from django.contrib.auth.models import User  
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    salary = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    applied_for = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.applied_for})"
