from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render
from django.views import View

from .models import Company, Specialty, Vacancy


def custom_handler404(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404</h1>Ой, что то сломалось... Наша команда уже чинит эту проблему!')


def custom_handler500(request):
    return HttpResponseServerError('<h1>Ошибка 500</h1>Не перживайте, вы все делали правильно. '
                                   'Но мы этого не предусмотрели, уже чиним!')


class IndexView(View):
    def get(self, request):
        context = {
            "jobs": Vacancy.objects.all(),
            "specialties": Specialty.objects.all(),
            "companies": Company.objects.all(),
        }
        return render(request, "index.html", context)


class VacanciesView(View):
    def get(self, request):
        context = {
            "jobs": Vacancy.objects.all(),
        }
        return render(request, "all_vacancies.html", context)


class VacanciesCategoryView(View):
    def get(self, request, vacancy_category):
        context = {
            "jobs": Vacancy.objects.filter(specialty__code__contains=vacancy_category),
            "specialty_title": Specialty.objects.filter(code__contains=vacancy_category).first().title
        }
        return render(request, "vacancies.html", context)


class CompanyView(View):
    def get(self, request, company_id):
        if company_id not in range(1, Company.objects.all().count() + 1):
            raise Http404
        context = {
            "company": Company.objects.get(id=company_id),
            "jobs": Vacancy.objects.filter(company__id=company_id),
        }
        return render(request, "company.html", context)


class VacancyView(View):
    def get(self, request, vacancy_id):
        if vacancy_id not in range(1, Vacancy.objects.all().count() + 1):
            raise Http404
        context = {
            "job": Vacancy.objects.get(id=vacancy_id)
        }
        return render(request, "vacancy.html", context)


class CreateCompanyView(View):
    def get(self, request):
        return render(request, 'company-create.html')


class CompaniesView(View):
    def get(self, request):
        context = {
            "companies": Company.objects.all(),
        }
        return render(request, "all_companies.html", context)
