from django.db import models

import data


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50)
    logo = models.ImageField()
    description = models.TextField()
    employee_count = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name}"


class Specialty(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=50, unique=True)
    picture = models.ImageField()

    def __str__(self):
        return f"{self.title}"


class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, related_name="vacancies", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="vacancies", on_delete=models.CASCADE)
    skills = models.CharField(max_length=500)
    description = models.CharField(max_length=300)
    salary_min = models.SmallIntegerField()
    salary_max = models.SmallIntegerField()
    published_at = models.DateField()

    def __str__(self):
        return f"{self.title}"


def populate_db():
    """
    function to populate database with info

    In shell_plus type:

    from jobs.models import *
    populate_db()

    """
    for specialty in data.specialties:
        Specialty.objects.create(title=specialty.get("title"),
                                 code=specialty.get("code"),
                                 picture=specialty.get("picture")
                                 )

    for company in data.companies:
        Company.objects.create(name=company.get("title"),
                               location=company.get("location"),
                               logo=company.get("logo"),
                               description=company.get("description"),
                               employee_count=company.get("employee_count")
                               )

    for job in data.jobs:
        Vacancy.objects.create(
            title=job.get("title"),
            # Мне пришлось использовать __contains, потому что компании evilthreat и hirey попадают в БД с пробелами
            specialty=Specialty.objects.get(title__contains=job.get("cat")),
            company=Company.objects.get(name__contains=job.get("company")),
            skills=job.get("skills"),
            description=job.get("desc"),
            salary_min=job.get("salary_from"),
            salary_max=job.get("salary_to"),
            published_at=job.get("posted")
        )
