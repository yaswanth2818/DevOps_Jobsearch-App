from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sector/<int:sector_id>/', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
]
