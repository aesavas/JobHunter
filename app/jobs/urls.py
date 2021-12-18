from django.conf.urls import url
from django.urls import path
from . import apps

from .views import (
    landing_page_view,
    dashboard_view,
    add_job_post_view,
    delete_job_post_view,
    add_resume_view,
    delete_resume_view
)

app_name = "apps.JobsConfig.name"

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('add-job-post/', add_job_post_view, name='add-job-post'),
    path('delete-job-post/<str:id>', delete_job_post_view, name='delete-job-post'),
    path('add-resume/', add_resume_view, name='add-resume'),
    path('delete-resume/<str:id>', delete_resume_view, name='delete-resume'),
]
