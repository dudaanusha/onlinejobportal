from django.contrib import admin
from django.urls import path
from JobApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('jobs/', views.job_listings, name='job_listings'),
    path('apply/<int:job_id>/', views.application_form, name='application_form'),
    path('success/', views.application_success, name='success'),
    path('my_applications/', views.my_applications, name='my_applications'),
    path('add_job/', views.add_job, name='add_job'),  
]
