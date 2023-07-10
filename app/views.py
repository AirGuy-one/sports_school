import os

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
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
    file_path = os.path.join(settings.MEDIA_ROOT, request.GET.get('filename'))
    file_name = str(request.GET.get('filename')).split('/')[-1]
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
    document_name = get_object_or_404(Document, title='Положение_Академии_футбола').file
    return render(request, 'structure_and_management.html', {'document_name': document_name})


def available_environment(request):
    return render(request, 'available_environment.html')


def documents(request):
    docs = Document.objects.filter(pk__range=(1, 29)).select_related('category')
    anti_doping = Document.objects.filter(pk__range=(30, 32)).select_related('category')
    anti_terror = Document.objects.filter(pk__range=(33, 36)).select_related('category')
    personal_data_security = Document.objects.filter(pk__range=(38, 41)).select_related('category')
    info_for_parents = Document.objects.filter(pk__range=(42, 49)).select_related('category')

    medical_activity = Document.objects.filter(Q(pk=1) | Q(pk=50)).select_related('category')
    name_changing = Document.objects.filter(pk__range=(51, 52)).select_related('category')

    anti_corruption = Document.objects.filter(pk__range=(53, 58)).select_related('category')

    context = {
        'docs': docs,
        'anti_doping': anti_doping,
        'anti_terror': anti_terror,
        'personal_data_security': personal_data_security,
        'info_for_parents': info_for_parents,
        'medical_activity': medical_activity,
        'name_changing': name_changing,
        'anti_corruption': anti_corruption
    }
    return render(request, 'documents.html', context)


def education(request):
    title_of_document = 'Дополнительная_образовательная_программа_спортивной_подготовки_по_виду_спорта_футбол'
    document_name = get_object_or_404(Document, title=title_of_document).file
    return render(request, 'education.html', {'document_name': document_name})


def financial_and_economic(request):
    state_order_title = 'ГЗ_2023'
    state_order_document_name = get_object_or_404(Document, title=state_order_title).file
    plan_title = 'ПФХД_на_2023'
    plan_document_name = get_object_or_404(Document, title=plan_title).file
    context = {
        'state_order_document_name': state_order_document_name,
        'plan_document_name': plan_document_name
    }
    return render(request, 'financial_and_economic.html', context)


def international_cooperation(request):
    return render(request, 'international_cooperation.html')


def paid_services(request):
    title_of_document = 'положение_о_порядке_поступления_и_использования_средств,_полученных_от_предпринимательской_и_иной_приносящей_доход_деятельности'
    document_name = get_object_or_404(Document, title=title_of_document).file
    return render(request, 'paid_services.html', {'document_name': document_name})


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
    appeal_commission_document_name = get_object_or_404(Document, title=appeal_commission_title).file
    individual_selection_title = 'Положение_о_порядке_проведении_индивидуального_отбора'
    individual_selection_document_name = get_object_or_404(Document, title=individual_selection_title).file
    receiving_commission_title = 'Положение_о_приемной_комиссии'
    receiving_commission_document_name = get_object_or_404(Document, title=receiving_commission_title).file
    admission_procedure_title = 'Порядок_приема_в_ГБУ_ДО_КО_СШ_им.Ярцева'
    admission_procedure_document_name = get_object_or_404(Document, title=admission_procedure_title).file
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
