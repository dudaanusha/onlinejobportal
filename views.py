from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Job, JobApplication

def home(request):
    if Job.objects.count() == 0:
        sample_jobs = [
            {"title": "Store Manager", "location": "Hyderabad", "category": "Management", "salary": "₹45,000"},
            {"title": "Cashier", "location": "Vijayawada", "category": "Finance", "salary": "₹18,000"},
            {"title": "Inventory Assistant", "location": "Vizag", "category": "Logistics", "salary": "₹20,000"},
            {"title": "Customer Support Executive", "location": "Guntur", "category": "Support", "salary": "₹22,000"},
            {"title": "Delivery Executive", "location": "Rajahmundry", "category": "Delivery", "salary": "₹19,000"},
            {"title": "Billing Assistant", "location": "Tirupati", "category": "Finance", "salary": "₹21,000"},
            {"title": "Warehouse Helper", "location": "Kurnool", "category": "Logistics", "salary": "₹16,000"},
            {"title": "Assistant Store Manager", "location": "Nellore", "category": "Management", "salary": "₹30,000"},
            {"title": "Security Staff", "location": "Eluru", "category": "Security", "salary": "₹17,000"},
            {"title": "Cleaner", "location": "Anantapur", "category": "Maintenance", "salary": "₹13,000"},
        ]
        for job in sample_jobs:
            Job.objects.create(
                title=job["title"],
                location=job["location"],
                category=job["category"],
                salary=job["salary"],
                created_at=timezone.now()
            )
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pswd = request.POST['pswd']
        user = authenticate(request, username=uname, password=pswd)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {uname}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('home')

def job_listings(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'job_listings.html', {'jobs': jobs})

@login_required(login_url='login')
def application_form(request, job_id):
    job = Job.objects.get(id=job_id)

    if request.method == 'POST':
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        message_text = request.POST.get('message')
        resume_file = request.FILES.get('resume')

        
        JobApplication.objects.create(
            user=request.user,
            applied_for=job,
            name=name,
            email=email,
            phone=phone,
            location=location,
            message=message_text,
            resume=resume_file
        )

        messages.success(request, "Application submitted successfully.")
        return redirect('success')

    return render(request, 'application_form.html', {'job': job, 'job_id': job_id})

def application_success(request):
    return render(request, 'success.html')

@login_required(login_url='login')
def my_applications(request):
   
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'my_applications.html', {'applications': applications})

def add_job(request):
    if request.method == "POST":
        title = request.POST.get("title")
        location = request.POST.get("location")
        category = request.POST.get("category")
        salary = request.POST.get("salary")
        Job.objects.create(
            title=title,
            location=location,
            category=category,
            salary=salary,
            created_at=timezone.now()
        )
        return redirect('job_listings')
    return render(request, 'add_job.html')
