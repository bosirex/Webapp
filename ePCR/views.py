from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EPCR
from .serializers import EPCRSerializer
from django.http import JsonResponse

@api_view(['POST'])
def submit_epcr(request):
    serializer = EPCRSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#empty form
# ePCR/views.py
# Add this to your existing imports


# ... existing views ...

def get_incident_data(request, incident_number):
    try:
        epcr = EPCR.objects.get(incident_number=incident_number)
        data = {
            'first_name': epcr.first_name,
            'last_name': epcr.last_name,
            'dob': epcr.dob,
            'gender': epcr.gender,
            # Add other fields as needed
        }
        return JsonResponse(data)
    except EPCR.DoesNotExist:
        return JsonResponse({'error': 'Incident not found'}, status=404)

def epcr_home(request):
    incident_numbers = EPCR.objects.all().order_by('-id')
    return render(request, 'epcr_form.html', {'incident_numbers': incident_numbers})
