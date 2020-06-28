from django.shortcuts import render
from django.views import View

from .models import Company, Specialty, Vacancy


class IndexView(View):
    def get(self, request):
        context = {
            "jobs": Vacancy.objects.all(),
            "specialties": Specialty.objects.all(),
            "companies": Company.objects.all(),
        }
        # context = {
        #     # context for jobs
        #     "frontend_jobs": Vacancy.objects.filter(specialty__title="Фронтенд"),
        #     "frontend_logo": Specialty.objects.filter(title="Фронтенд").first().picture,
        #
        #     "backend_jobs": Vacancy.objects.filter(specialty__title="Бэкенд"),
        #     "backend_logo": Specialty.objects.filter(title="Бэкенд").first().picture,
        #
        #     "gamedev_jobs": Vacancy.objects.filter(specialty__title="Геймдев"),
        #     "gamedev_logo": Specialty.objects.filter(title="Геймдев").first().picture,
        #
        #     "devops_jobs": Vacancy.objects.filter(specialty__title="Девопс"),
        #     "devops_logo": Specialty.objects.filter(title="Девопс").first().picture,
        #
        #     "design_jobs": Vacancy.objects.filter(specialty__title="Дизайн"),
        #     "design_logo": Specialty.objects.filter(title="Дизайн").first().picture,
        #
        #     "products_jobs": Vacancy.objects.filter(specialty__title="Продукты"),
        #     "products_logo": Specialty.objects.filter(title="Продукты").first().picture,
        #
        #     "management_jobs": Vacancy.objects.filter(specialty__title="Менеджмент"),
        #     "management_logo": Specialty.objects.filter(title="Менеджмент").first().picture,
        #
        #     "testing_jobs": Vacancy.objects.filter(specialty__title="Тестирование"),
        #     "testing_logo": Specialty.objects.filter(title="Тестирование").first().picture,
        #
        #     # context for companies
        #     "workiro_vacancies": Vacancy.objects.filter(company__name__contains="workiro"),
        #     "workiro_logo": Company.objects.filter(name__contains="workiro").first().logo,
        #
        #     "rebelrage_vacancies": Vacancy.objects.filter(company__name__contains="rebelrage"),
        #     "rebelrage_logo": Company.objects.filter(name__contains="rebelrage").first().logo,
        #
        #     "staffingsmarter_vacancies": Vacancy.objects.filter(company__name__contains="staffingsmarter"),
        #     "staffingsmarter_logo": Company.objects.filter(name__contains="staffingsmarter").first().logo,
        #
        #     "evilthreat_vacancies": Vacancy.objects.filter(company__name__contains="evilthreat"),
        #     "evilthreat_logo": Company.objects.filter(name__contains="evilthreat").first().logo,
        #
        #     "hirey_vacancies": Vacancy.objects.filter(company__name__contains="hirey"),
        #     "hirey_logo": Company.objects.filter(name__contains="hirey").first().logo,
        #
        #     "swiftattack_vacancies": Vacancy.objects.filter(company__name__contains="swiftattack"),
        #     "swiftattack_logo": Company.objects.filter(name__contains="swiftattack").first().logo,
        #
        #     "troller_vacancies": Vacancy.objects.filter(company__name__contains="troller"),
        #     "troller_logo": Company.objects.filter(name__contains="troller").first().logo,
        #
        #     "primalassault_vacancies": Vacancy.objects.filter(company__name__contains="primalassault"),
        #     "primalassault_logo": Company.objects.filter(name__contains="primalassault").first().logo,
        #
        #
        # }
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
        context = {
            "company": Company.objects.get(id=company_id),
            "jobs": Vacancy.objects.filter(company__id=company_id),
        }
        return render(request, "company.html", context)


class VacancyView(View):
    def get(self, request, vacancy_id):
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
