"""ayekah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.urls import path
from .views import home_page, about_page, sign_up_page,login_page, register_page, donate_page
from emails.views import twillio_page, confirm_page


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('about/', about_page, name = 'about'),
    path('signup/', sign_up_page, name = 'signup'),
    path('login/', login_page, name = 'login'),
    path('register/', register_page, name = 'register'),
    path('twillio/', twillio_page, name = 'twillio'),
    path('confirm/', confirm_page, name = 'confirm'),
    path('donate/', donate_page, name = 'donate')

] +  staticfiles_urlpatterns()
