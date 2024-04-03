# urls.py in your Django project
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('pdf/generate_pdf/', views.generate_pdf, name='generate_pdf'),
]
