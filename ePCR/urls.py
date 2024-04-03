from django.urls import path, include
from . import views

# ePCR/urls.py


urlpatterns = [
    path('', views.epcr_home, name='epcr_home'),
    path('submit_epcr/', views.submit_epcr, name='submit_epcr'),
    path('get-incident-data/<str:incident_number>/', views.get_incident_data, name='get_incident_data'),
]
'''
urlpatterns = [
    #path('submit_epcr/', views.submit_epcr, name='submit_epcr'),
    #path('epcrform/', epcrform, name='epcr_form'),
    #path('odform/', odform, name='od_form'),
    #path('overdose_form/', overdose_form_view, name='overdose_form'),
]'''
