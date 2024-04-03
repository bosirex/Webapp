from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (assign_responder, home, report_incident, index, indextwo,
                    icviews, status_update, approved_users, credential_list,
                    get_credentials, update_credential, add_credential, create_employee,
                    status_update_credential, incidents_view, need_help_list_create,
                    manuel_manage_incident, record_incident, save_coords, get_marker,
                    message_board, RecMsgAPI,fetch_assignment)

urlpatterns = [
    path('assign_responder/', assign_responder, name='assign_responder'),
    path('home/', home, name='home'),
    path('report_incident/', report_incident, name='report_incident'),
    path('index/', index, name='index'),
    path('indextwo/', indextwo, name='indextwo'),
    path('icviews/', icviews, name='icviews'),

    # API section
    path('status_update/', status_update, name='status_update'),
    path('api/approved_users/', approved_users, name='approved_users_api'),
    path('api/credentials/', credential_list, name='credential-list'),
    path('get_credentials/', get_credentials, name="get_credentials"),
    path('update/', update_credential, name='update_credential'),
    path('add/', add_credential, name='add_credential'),
    path('update_credential/<str:username>/', update_credential, name='update_credential_by_username'),


    # Other sections
    path('create_employee/', create_employee, name='create_employee'),
    path('status_update_credential/<str:username>/', status_update_credential, name='status_update_credential'),
    path('incidents_view/', incidents_view, name='incidents_view'),
    path('api/need_help_list/', need_help_list_create, name='need_help_list_api'),
    path('manuel_help_on_way/', manuel_manage_incident, name='manuel_manage_incident'),
    path('needhelp/', need_help_list_create, name='needhelp-list-create'),

    # Text message URLs
    path('record_incident/', record_incident, name='record_incident'),
    path('save_coords/', save_coords, name='save_coords'),
    path('get_marker/', get_marker, name='get_marker'),
    path('message_board/', message_board, name='message_board'),
    #path('rec_msg/', RecMsgAPI.as_view(), name='rec_msg'),
    path('fetch_assignment/<str:username>/', fetch_assignment, name='fetch_assignment_user'),
    #path('message-board/', views.message_board, name='message_board'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
