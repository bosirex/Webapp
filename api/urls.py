from django.urls import path
from . import views

urlpatterns = [
    path('update/<str:username>/', views.update_credential, name='update_credential'),
    path('login_gps/', views.login_gps, name='login_gps'),



    ]
    # ... other url patterns ...