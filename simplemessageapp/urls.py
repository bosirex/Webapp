from django.urls import path
from . import views

app_name = 'simplemessageapp'

urlpatterns = [
    path('api/messages/', views.message_list, name='message-list'),
    path('send_message/', views.SendMessageView.as_view(), name='send-message'),
]
