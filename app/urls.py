from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('basic_info', views.basic_info, name='basic_info_url'),
    path('structure_management', views.structure_management, name='structure_management_url'),
    path('available_environment', views.available_environment, name='available_environment_url'),
    path('documents', views.documents, name='documents_url'),
    path('education', views.education, name='education_url'),
    path('financial_and_economic', views.financial_and_economic, name='financial_and_economic_url'),
    path('international_cooperation', views.international_cooperation, name='international_cooperation_url'),
    path('paid_services', views.paid_services, name='paid_services_url'),
    path('pedagogical_staff', views.pedagogical_staff, name='pedagogical_staff_url'),
    path('support_and_equipment', views.support_and_equipment, name='support_and_equipment_url'),
    path('vacant_seats', views.vacant_seats, name='vacant_seats_url'),
    path('contacts', views.contacts, name='contacts_url'),
]
