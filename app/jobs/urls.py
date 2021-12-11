from django.conf.urls import url
from django.urls import path
from . import apps

from .views import (
    landing_page_view,
)

app_name = "apps.JobsConfig.name"

urlpatterns = [
    path('', landing_page_view, name='landing-page'),
]
