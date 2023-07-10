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
    document_name = str(get_object_or_404(Document, title='Положение_Академии_футбола').file).split('/')[-1]
    return render(request, 'structure_and_management.html', {'document_name': document_name})


def available_environment(request):
    return render(request, 'available_environment.html')


def documents(request):
    docs = Document.objects.filter(pk__range=(13, 29)).select_related('category')
    return render(request, 'documents.html', {'docs': docs})


def education(request):
    title_of_document = 'Дополнительная_образовательная_программа_спортивной_подготовки_по_виду_спорта_футбол'
    document_name = str(get_object_or_404(Document, title=title_of_document).file).split('/')[-1]
    return render(request, 'education.html', {'document_name': document_name})


def financial_and_economic(request):
    state_order_title = 'ГЗ_2023'
    state_order_document_name = str(get_object_or_404(Document, title=state_order_title).file).split('/')[-1]
    plan_title = 'ПФХД_на_2023'
    plan_document_name = str(get_object_or_404(Document, title=plan_title).file).split('/')[-1]
    context = {
        'state_order_document_name': state_order_document_name,
        'plan_document_name': plan_document_name
    }
    return render(request, 'financial_and_economic.html', context)


def international_cooperation(request):
    return render(request, 'international_cooperation.html')


def paid_services(request):
    title_of_document = 'положение_о_порядке_поступления_и_использования_средств,_полученных_от_предпринимательской_и_иной_приносящей_доход_деятельности'
    document_name = str(get_object_or_404(Document, title=title_of_document).file).split('/')[-1]
    context = {
        'document_name': document_name
    }
    return render(request, 'paid_services.html', context)


def pedagogical_staff(request):
    return render(request, 'pedagogical_staff.html')


def support_and_equipment(request):
    return render(request, 'support_and_equipment.html')


def vacant_seats(request):
    return render(request, 'vacant_seats.html')


def contacts(request):
    return render(request, 'contacts.html')


def admission_conditions(request):
    appeal_commission_title = 'Положение_об_апелляционной_комиссии'
    appeal_commission_document_name = str(get_object_or_404(Document, title=appeal_commission_title).file).split('/')[-1]
    individual_selection_title = 'Положение_о_порядке_проведении_индивидуального_отбора'
    individual_selection_document_name = str(
        get_object_or_404(Document, title=individual_selection_title).file).split('/')[-1]
    receiving_commission_title = 'Положение_о_приемной_комиссии'
    receiving_commission_document_name = str(
        get_object_or_404(Document, title=receiving_commission_title).file).split('/')[-1]
    admission_procedure_title = 'Порядок_приема_в_ГБУ_ДО_КО_СШ_им.Ярцева'
    admission_procedure_document_name = str(
        get_object_or_404(Document, title=admission_procedure_title).file).split('/')[-1]
    context = {
        'appeal_commission_document_name': appeal_commission_document_name,
        'individual_selection_document_name': individual_selection_document_name,
        'receiving_commission_document_name': receiving_commission_document_name,
        'admission_procedure_document_name': admission_procedure_document_name,
    }
    return render(request, 'admission_conditions.html', context)


def catering(request):
    return render(request, 'catering.html')


def educational_standards_and_requirements(request):
    return render(request, 'educational_standards_and_requirements.html')
