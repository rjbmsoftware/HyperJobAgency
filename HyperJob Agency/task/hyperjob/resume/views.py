from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.db.models import Manager
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.base import TemplateView, View
from resume.models import Resume


class ResumesPage(TemplateView):
    template_name = 'resume/resumes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumes'] = Resume.objects.all()

        return context


class HomepageProfileView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return HttpResponseRedirect('vacancy/new')
            else:
                return HttpResponseRedirect('resume/new')
        else:
            context = {'links': []}
            return render(request=request, template_name='resume/profile_page.html', context=context)


class UpdateResume(View):

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='resume/update_resume.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            resume_manager: Manager = Resume.objects  # need to test for new user
            resume = resume_manager.filter(author=request.user).first()
            if resume:
                resume.description = request.POST['description']
                resume.save()
            else:
                resume_manager.create(author=request.user, description=request.POST['description'])

            return HttpResponseRedirect('/home')
        else:
            return HttpResponse('Unauthorised', status=403)


class SignupPageView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'resume/signup.html'


class LoginPageView(LoginView):
    redirect_authenticated_user = True
    template_name = 'resume/login.html'
