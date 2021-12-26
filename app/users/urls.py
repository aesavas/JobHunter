from django.urls import path
from . import apps
from .views import (
    delete_skill_view,
    sign_up_view,
    login_view,
    logout_view,
    account_view,
    edit_account_view,
    edit_password_view,
    add_skill_view,
    delete_skill_view,
)

app_name = "apps.UsersConfig.name"

urlpatterns = [
    path('sign-up/', sign_up_view, name='sign-up'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change-password/', edit_password_view, name='edit-password'),
    path('', account_view, name='account'), #! Id will add to url
    path('edit/', edit_account_view, name='edit-account'), #! Id will add to url
    path('add-skill/', add_skill_view, name='add-skill'),
    path('delete-skill/<str:id>/', delete_skill_view, name='delete-skill'),
]
