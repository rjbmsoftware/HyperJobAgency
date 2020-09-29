"""menu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from menu.views import Homepage
from resume.views import ResumesPage, SignupPageView, LoginPageView, HomepageProfileView, UpdateResume
from vacancy.views import VacanciesPage, UpdateVacancy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view()),
    path('resumes', ResumesPage.as_view()),
    path('vacancies', VacanciesPage.as_view()),
    path('signup', SignupPageView.as_view()),
    path('login', LoginPageView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('home', HomepageProfileView.as_view()),
    path('resume/new', UpdateResume.as_view()),
    path('vacancy/new', UpdateVacancy.as_view())
]
