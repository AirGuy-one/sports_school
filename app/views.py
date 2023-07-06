import os

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from urllib.parse import quote

from .models import News, Games, Document, DocumentCategory


def index(request):
    news_from_db = News.objects.all().order_by('-id').prefetch_related('photos')
    games = Games.objects.all()

    context = {
        'news': news_from_db,
    }

    return render(request, 'index.html', context)


def download_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, f"files/{request.GET.get('category')}/{request.GET.get('filename')}")
    file_name = request.GET.get('filename')
    encoded_file_name = quote(file_name)

    with open(file_path, 'rb') as file:
        file_content = file.read()

    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{encoded_file_name}"'

    response.write(file_content)
    return response


def news(request):
    news_from_db = News.objects.all().order_by('-id').prefetch_related('photos')
    games = Games.objects.all()

    context = {
        'news': news_from_db,
    }

    return render(request, 'news.html', context)


def basic_info(request):
    return render(request, 'basic_information.html')


def structure_management(request):
    return render(request, 'structure_and_management.html')


def available_environment(request):
    return render(request, 'available_environment.html')


def documents(request):
    context = {
        'extract_from_register': str(get_object_or_404(Document, pk=1).file).split('/')[-1],
        'logo_regulations': str(get_object_or_404(Document, pk=2).file).split('/')[-1],
        'inn': str(get_object_or_404(Document, pk=3).file).split('/')[-1],
        'additional_educational_program': str(get_object_or_404(Document, pk=4).file).split('/')[-1]
    }
    return render(request, 'documents.html', context)


def education(request):
    document = Document.objects.last()
    document_name = str(document.file).split('/')[-1]
    return render(request, 'education.html', {'document_name': document_name})


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


def contacts(request):
    return render(request, 'contacts.html')


def admission_conditions(request):
    return render(request, 'admission_conditions.html')
