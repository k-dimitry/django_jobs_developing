def statistics(request):
    context = {
        'navbar': [
            {'name': 'Вакансии', 'link': '/vacancies'},
            {'name': 'Компании', 'link': '/companies'},
            {'name': 'О проекте', 'link': '/about'},
        ],
    }
    return context
