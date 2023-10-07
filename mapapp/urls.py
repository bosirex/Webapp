from django.urls import path
from . import views
from .views import ReceiveMessageAPI

urlpatterns = [
    #path('credential_count/', views.credential_count, name='credential_count'),
    path('assign_responder/', views.assign_responder, name='assign_responder'),  # Add this line
    path('home/', views.home, name='home'),
    path('report_incident/', views.incident_report, name='report_incident'),
    #path('', views.home_view, name='home'),
    path('index/', views.index, name='index'),
    path('indextwo/', views.indextwo, name='indextwo'),
    path('icviews/', views.icviews, name='icviews'),
    #APi section
    path('status_update/', views.status_update, name='status_update'),
    path('api/approved_users/', views.approved_users, name='approved_users_api'),
    path('api/credentials/', views.credential_list, name='credential-list'),
    path('get_credentials/', views.get_credentials, name="get_credentials"),
    path('update/', views.update_credential, name='update_credential'),
    path('add/', views.add_credential, name='add_credential'),
    path('update_credential/<str:username>/', views.update_credential, name='update_credential_by_username'),
    #End Api Section
    # Login & Registration
    #path('register_user', views.register_user, name='register_user'),
    #End login & Registration End
    path('create_employee/', views.create_employee, name='create_employee'),
    path('status_update_credential/<str:username>/', views.status_update_credential, name='status_update_credential'),
    path('incidents_view/', views.incidents_view, name='incidents_view'),
    path('api/need_help_list/', views.need_help_list_create, name='need_help_list_api'),
    path('manuel_help_on_way/', views.manuel_manage_incident, name='manuel_manage_incident'),
    path('needhelp/', views.need_help_list_create, name='needhelp-list-create'),
    path('incidents_view/', views.incidents_view, name='incidents_view'),
    #text message urls
    path('record_incident/', views.record_incident, name='record_incident'),
    path('save_coords/', views.save_coords, name='save_coords'),
    #path('record_incident/', views.record_incident, name='record_incident'),
    path('get_marker/', views.get_marker, name='get_marker'),
    #path('msg_txt/', views.msg_txt, name='msg_txt'),
    path('message_board/', views.message_board, name='message_board'),
    #path('receive_message/', views.ReceiveMessageAPI.as_view(), name='receive_message_api'),
    # ... Recieve message from responder app
    path('rec_msg/', ReceiveMessageAPI.as_view(), name='rec_msg'),
]