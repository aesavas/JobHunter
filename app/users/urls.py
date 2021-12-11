from django.urls import path
from . import apps
from .views import (
    sign_up_view,
    login_view,
)

app_name = "apps.UsersConfig.name"

urlpatterns = [
    path('sign-up/', sign_up_view, name='sign-up'),
    path('login/', login_view, name='login'),
]
