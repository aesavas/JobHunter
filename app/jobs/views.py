from django.shortcuts import render

# Create your views here.
def landing_page_view(request):
    return render(request, 'jobs/index.html')


def dashboard_view(request):
    profile = request.user.profile
    jobs = profile.job_set.all()
    resumes = profile.resume_set.all()
    status_count = {
        'applied' : jobs.filter(status="Applied").count(),
        'phone' : jobs.filter(status="Phone Interview").count(),
        'technical' : jobs.filter(status="Technical Interview").count(),
        'offer' : jobs.filter(status="Offer").count(),
        'rejected' : jobs.filter(status="Rejected").count(),
    }
    context = {
        'profile' : profile,
        'jobs' : jobs,
        'resumes' : resumes,
        'status_count':status_count,
    }
    return render(request, 'jobs/dashboard.html', context)