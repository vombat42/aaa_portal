from django.shortcuts import render

from aaa_portal import settings

# ------------------------------------------------------------------------

def index(request):
    data = {
        'title': 'Проект \"Коммуна\"',
        # 'styles': '/css/styles.css',
    }
    return render(request, 'commune/index.html', data)


def about(request):
    data = {
        'title': 'О проекте \"Коммуна\"',
        # 'styles': '/css/styles.css',
    }
    return render(request, 'commune/about.html', data)