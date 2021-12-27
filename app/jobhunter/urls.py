"""jobhunter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#! Landing page
from jobs.views import landing_page_view

from users.forms import UserPasswordResetForm, UserPasswordSetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='auth')),
    path('account/', include('users.urls', namespace='account')),
    path('', landing_page_view, name='landing-page'),
    path('dashboard/', include('jobs.urls', namespace='dashboard')),
    path('reset_password/', PasswordResetView.as_view(template_name='users/reset_password.html', form_class=UserPasswordResetForm), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='users/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/reset.html', form_class=UserPasswordSetForm), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='users/reset_password_complete.html'), name='password_reset_complete'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)