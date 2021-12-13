from django.urls import path
from . import apps
from .views import (
    sign_up_view,
    login_view,
    logout_view,
    account_view,
)

app_name = "apps.UsersConfig.name"

urlpatterns = [
    path('sign-up/', sign_up_view, name='sign-up'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', account_view, name='account'), #! Id will add to url
]
