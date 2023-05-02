from django.shortcuts import render
from .models import News, Games


def index(request):
    news = News.objects.all().order_by('-id').prefetch_related('photos')
    games = Games.objects.all()

    context = {
        'news': news,
    }

    return render(request, 'index.html', context)


def basic_info(request):
    return render(request, 'basic_information.html')


def structure_management(request):
    return render(request, 'structure_and_management.html')


def available_environment(request):
    return render(request, 'available_environment.html')


def documents(request):
    return render(request, 'documents.html')


def education(request):
    return render(request, 'education.html')


def financial_and_economic(request):
    return render(request, 'financial_and_economic.html')


def international_cooperation(request):
    return render(request, 'international_cooperation.html')


def paid_services(request):
    return render(request, 'paid_services.html')


def pedagogical_staff(request):
    return render(request, 'pedagogical_staff.html')


def support_and_equipment(request):
    return render(request, 'support_and_equipment.html')


def vacant_seats(request):
    return render(request, 'vacant_seats.html')
