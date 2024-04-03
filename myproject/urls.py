from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('memeber', include('members.urls')),
    path('', include('members.urls')),
    path('', include('api.urls')),
    #path('', include('simplemessageapp.urls')),
    path('mapapp/', include('mapapp.urls')),
    path('simplemessageapp/', include('simplemessageapp.urls')),
    path('epcr/',include('ePCR.urls')),
    path('pdf/', include('pdf.urls')),





    #path('api/message/', include('Message_API.urls')),
    #path('api/messaging/', include('messaging.urls')),
]

