from django.shortcuts import render, get_object_or_404
from .models import Sector, Job

def home(request):
    sectors = Sector.objects.all()
    return render(request, 'jobs/home.html', {'sectors': sectors})

def job_list(request, sector_id):
    sector = get_object_or_404(Sector, id=sector_id)
    jobs = Job.objects.filter(sector=sector)
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'sector': sector})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})
