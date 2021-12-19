from django.conf.urls import url
from django.urls import path
from . import apps

from .views import (
    landing_page_view,
    dashboard_view,
    add_job_post_view,
    delete_job_post_view,
    edit_job_post_view,
    add_resume_view,
    delete_resume_view,
    edit_resume_view,
    detail_resume_view,
)

app_name = "apps.JobsConfig.name"

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('add-job-post/', add_job_post_view, name='add-job-post'),
    path('delete-job-post/<str:id>', delete_job_post_view, name='delete-job-post'),
    path('edit-job-post/<str:id>', edit_job_post_view, name='edit-job-post'),
    path('add-resume/', add_resume_view, name='add-resume'),
    path('delete-resume/<str:id>', delete_resume_view, name='delete-resume'),
    path('edit-resume/<str:id>', edit_resume_view, name='edit-resume'),
    path('detail-resume/<str:id>', detail_resume_view, name='detail-resume'),
]
