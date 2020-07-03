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
        return render(request, "vacancies.html", context)


class VacanciesCategoryView(View):
    def get(self, request, vacancy_category):
        # Создаём список со всеми категориями из базы
        specialties_codes_list = [spec.code for spec in Specialty.objects.all()]

        # Проверяем, что у нас есть запрошенная категория
        if vacancy_category not in specialties_codes_list:
            raise Http404

        context = {
            "jobs": Vacancy.objects.filter(specialty__code__contains=vacancy_category),
            "specialty_title": Specialty.objects.filter(code__contains=vacancy_category).first().title
        }
        return render(request, "vacancies_by_specialty.html", context)


class CompanyView(View):
    def get(self, request, company_id):
        # Создаём список всех id компаний из базы
        companies_ids_list = [comp.id for comp in Company.objects.all()]

        # Проверяем, что у нас есть компания с запрошенным id
        if company_id not in companies_ids_list:
            raise Http404

        context = {
            "company": Company.objects.get(id=company_id),
            "jobs": Vacancy.objects.filter(company__id=company_id),
        }
        return render(request, "company.html", context)


class VacancyView(View):
    def get(self, request, vacancy_id):
        # Создаём список со всеми id вакансий из базы
        vacancies_ids_list = [job.id for job in Vacancy.objects.all()]

        # Проверяем, что у нас есть вакансия с запрошенным id
        if vacancy_id not in vacancies_ids_list:
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
        return render(request, "companies.html", context)


class AboutView(View):
    def get(self, request):
        return render(request, "about.html")
