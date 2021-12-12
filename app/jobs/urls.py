from django.conf.urls import url
from django.urls import path
from . import apps

from .views import (
    landing_page_view,
    dashboard_view
)

app_name = "apps.JobsConfig.name"

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
]
