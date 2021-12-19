from django.contrib import messages
from django.shortcuts import render, redirect

#! Models
from .models import Job, Resume

"""
!TODO LIST:
?Add Job Form
?Add Resume Form
?Add Skill Form
?Menu Links
?Detail Page
?Edit and Delete Pages
?Edit and Delete Buttons on dashboard table.
"""


# Create your views here.
def landing_page_view(request):
    return render(request, 'jobs/index.html')


def dashboard_view(request):
    profile = request.user.profile
    jobs = profile.job_set.all()
    resumes = profile.resume_set.all()
    skills = profile.skill_set.all()
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
        'skills': skills,
    }
    return render(request, 'jobs/dashboard.html', context)


def add_job_post_view(request):
    STATUS_CHOICE = [
        ('Applied','Applied'),
        ('Phone Interview','Phone Interview'),
        ('Technical Interview','Technical Interview'),
        ('Offer','Offer'),
        ('Rejected','Rejected'),
    ]
    if request.method == "POST":
        companyName = request.POST['companyName']
        jobTitle = request.POST['jobTitle']
        applyDate = request.POST['applyDate']
        applyPlatform = request.POST['applyPlatform']
        jobPost = request.POST['jobPost']
        applyStatus = request.POST['applyStatus']
        comments = request.POST['comments']
        job = Job.objects.create(
            owner=request.user.profile,
            company_name=companyName,
            job_title = jobTitle,
            apply_date = applyDate,
            apply_platform = applyPlatform,
            status = applyStatus,
            job_post = jobPost,
            notes = comments
        )
        job.save()
        messages.success(request, 'Your job post added successfully!')
        return redirect('dashboard:dashboard')
    context = {
        'STATUS_CHOICE': STATUS_CHOICE,
    }
    return render(request, 'jobs/add-job.html', context)


def delete_job_post_view(request, id):
    profile = request.user.profile
    job_post = profile.job_set.get(id=id)
    if request.method == "POST":
        job_post.delete()
        messages.success(request, 'Your job post deleted successfully!')
        return redirect('dashboard:dashboard')
    context = {
        'job_post':job_post
    }
    return render(request, 'jobs/delete-job.html', context)


def edit_job_post_view(request, id):
    STATUS_CHOICE = [
        ('Applied','Applied'),
        ('Phone Interview','Phone Interview'),
        ('Technical Interview','Technical Interview'),
        ('Offer','Offer'),
        ('Rejected','Rejected'),
    ]
    profile = request.user.profile
    job_post = profile.job_set.get(id=id)
    if request.method == "POST":
        companyName = request.POST['companyName']
        jobTitle = request.POST['jobTitle']
        applyDate = request.POST['applyDate']
        applyPlatform = request.POST['applyPlatform']
        jobPost = request.POST['jobPost']
        applyStatus = request.POST['applyStatus']
        comments = request.POST['comments']
        job_post.company_name=companyName
        job_post.job_title = jobTitle
        job_post.apply_date = applyDate
        job_post.apply_platform = applyPlatform
        job_post.status = applyStatus
        job_post.job_post = jobPost
        job_post.notes = comments
        job_post.save()
        messages.success(request, 'Your job post added successfully!')
        return redirect('dashboard:dashboard')
    context = {
        'job_post':job_post,
        'STATUS_CHOICE':STATUS_CHOICE,
    }
    return render(request, 'jobs/edit-job.html', context)


def add_resume_view(request):
    if request.method == "POST":
        resumeName = request.POST['resumeName']
        description = request.POST['description']
        resumeFile = request.FILES['resumeFile']
        resume = Resume.objects.create(
            owner = request.user.profile,
            resume_name = resumeName,
            description = description,
            resume_file = resumeFile
        )
        resume.save()
        return redirect('dashboard:dashboard')
    return render(request, 'jobs/add-resume.html')


def delete_resume_view(request, id):
    profile = request.user.profile
    resume = profile.resume_set.get(id=id)
    if request.method == "POST":
        resume.delete()
        messages.success(request, 'Your resume has been deleted successfully!')
        return redirect('dashboard:dashboard')
    context = {
        'resume' : resume
    }
    return render(request, 'jobs/delete-resume.html', context)


def edit_resume_view(request, id):
    profile = request.user.profile
    resume = profile.resume_set.get(id=id)
    if request.method == "POST":
        resumeName = request.POST['resumeName']
        resumeDescription = request.POST['description']
        resume.resume_name = resumeName
        resume.description = resumeDescription
        #TODO: This solution look like unprofessional, we need to change it.
        try:
            resumeFile = request.FILES['resumeFile']
            resume.resume_file = resumeFile
        except:
            pass
        resume.save()
        messages.success(request, 'Your resume details has been updated successfully!')
        return redirect('dashboard:dashboard')
    context = {
        'resume' : resume,
    }
    return render(request, 'jobs/edit-resume.html', context)


def detail_resume_view(request, id):
    profile = request.user.profile
    resume = profile.resume_set.get(id=id)
    context = {
        'resume':resume,
    }
    return render(request, 'jobs/detail-resume.html', context)