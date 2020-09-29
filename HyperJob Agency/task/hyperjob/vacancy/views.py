from django.db.models import Manager
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from vacancy.models import Vacancy


class VacanciesPage(TemplateView):
    template_name = 'vacancy/vacancies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context


class UpdateVacancy(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='resume/update_resume.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            vacancy_manager: Manager = Vacancy.objects
            vacancy = vacancy_manager.filter(author=request.user).first()
            if vacancy:
                vacancy.description = request.POST['description']
                vacancy.save()
            else:
                vacancy_manager.create(author=request.user, description=request.POST['description'])

            return HttpResponseRedirect('/home')
        else:
            return HttpResponse('Unauthorised', status=403)
