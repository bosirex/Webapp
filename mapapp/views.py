from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Credential, Incidents, needHelp
from .serializers import CredentialSerializer, StatusUpdateSerializer, IncidentSerializer,NeedHelpSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated  # Example permission
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import needHelp
from .serializers import NeedHelpSerializer
from django.shortcuts import render, redirect
from .forms import IncidentReportForm
from django.http import JsonResponse
import math
from .models import Credential, needHelp, Assignment  # Adjust the import as per your project structure
from django.utils import timezone




###Dispatch Controls###

def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 3959  # Radius of Earth in kilometers
    return c * r


def assign_responder(request):
    # Define the time window (e.g., 5 minutes)
    time_window = timezone.now() - timezone.timedelta(minutes=5)

    # Get all recent incidents within the time window
    recent_incidents = needHelp.objects.filter(timestamp__gte=time_window)

    # Create dictionaries to track incidents and responders
    incidents = {}
    responders = {}

    for incident in recent_incidents:
        area = incident.area

        # Check if the area is already being handled
        if area not in incidents:
            incidents[area] = []
            responders[area] = []

        incidents[area].append(incident)

    # Filter available responders (status='in_service')
    available_responders = Credential.objects.filter(status='in_service')

    for area, area_incidents in incidents.items():
        if len(area_incidents) >= 3:  # If there are 3 or more incidents in the same area
            if available_responders:
                # Assign one responder to all incidents in the area
                responder = available_responders.first()
                available_responders = available_responders.exclude(id=responder.id)
                responders[area].append(responder)

                for incident in area_incidents:
                    Assignment.objects.create(incident=incident, responder=responder, distance=0)

    # Count unassigned incidents
    unassigned_incidents_count = needHelp.objects.filter(assignment__isnull=True).count()

    # Ensure unassigned_incidents_count is set to 0 if there are no unassigned incidents
    if unassigned_incidents_count == None:
        unassigned_incidents_count = 0

    return JsonResponse({"status": "success", "unassigned_incidents_count": unassigned_incidents_count})
#beginning of text feature

def text_comm_view(request):
    # Retrieve all usernames from the Credential model
    all_users = Credential.objects.values_list('username', flat=True)

    context = {
        'all_users': all_users,
    }

    return render(request, 'home.html', context)


'''def home(request):
    # status update
    credentials_data = Credential.objects.all()
    context = {'credentials_data': credentials_data}

    total_responders = Credential.objects.all().count()
    context['total_responders'] = total_responders

    assignments_data = Assignment.objects.all()
    return render(request, 'mapapp/home.html', {'assignments_data': assignments_data})

    return render(request, 'mapapp/home.html', context)'''

# mapapp/views.py

from django.shortcuts import render
from .models import Credential, Assignment  # Ensure the necessary models are imported

#in_service
# Define the home view
def home(request):
    credentials_data = Credential.objects.all()
    total_responders = Credential.objects.all().count()
    assignments_data = Assignment.objects.all()
    all_users = Credential.objects.values_list('username', flat=True)
    in_service_responders = Credential.objects.filter(status='in_service')
    responder_all = Credential.objects.all()



    # Debugging: Print the fetched assignments_data to the console
    print(assignments_data)

    context = {
        'credentials_data': credentials_data,
        'total_responders': total_responders,
        'assignments_data': assignments_data,
        'all_users': all_users,
        'responders': in_service_responders,
        'responder_all':responder_all,
    }

    return render(request, 'mapapp/home.html', context)


from django.shortcuts import render
from django.http import JsonResponse


def get_marker(request):
    category = request.GET.get('category', 'other')

    marker_color_map = {
        'medical': 'marker-icon-2x-medical.png',
        'security': 'marker-icon-2x-inc.png',
        'spill': 'marker-icon-2x-spill.png',
        'other': 'marker-icon-2x-violet.png'
    }

    marker_image = marker_color_map.get(category, 'marker-icon-2x-violet.png')

    return JsonResponse({'marker_image': marker_image})


# ... [Other views you might have] ...


def index(request):
    return render(request, 'mapapp/map_one.html')

def indextwo(request):
    return render(request, 'mapapp/map_two.html')

def icviews(request):
    return render(request, 'mapapp/map_three.html')
# memberss sections
'''
def login_user(request):
    user = None  # Initialize user variable

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        messages.success(request, ("There was an error Try again"))
        #return render(request, 'your_template_name_here.html')  # Return a response even for non-POST requests

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Registration Successful"))

    else:
        form = UserCreationForm()

    return render(request, 'mapapp/register_user.html',
                  {'form': form,})
'''
#text message function #
# mapapp/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import needHelp, Credential
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def record_incident(request):
    if request.method == "POST":
        # Extract data from POST
        incident_number = request.POST.get('incident_number')
        category = request.POST.get('incident_type')
        responder = request.POST.get('responder')

        # Create needHelp instance
        help_record = needHelp(
            username=incident_number,
            category=category
        )
        help_record.save()

        # Render the map popup
        return render(request, 'mapapp/map_popup.html', {'help_record': help_record, 'responder_id': responder})

    return redirect('home')
# mapapp/views.py

@csrf_exempt
def save_coords(request):
    data = json.loads(request.body)
    incident = needHelp.objects.get(id=data['incident_id'])
    responder = Credential.objects.get(id=data['responder_id'])

    incident.latitude = data['incident_coords']['lat']
    incident.longitude = data['incident_coords']['lng']
    incident.save()

    responder.username = incident.username
    responder.latitude = data['responder_coords']['lat']
    responder.longitude = data['responder_coords']['lng']
    responder.acceleration = 1
    responder.save()

    return JsonResponse({'status': 'ok'})
###########

# end members section
def manuel_manage_incident(request):
    submitted = False
    if request.method == "POST":
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/IncidentsReportForm?submitted=True/')
    else:
        form = IncidentReportForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'mapapp/incidents.html',{'form':form,'submitted':submitted })


'''def status_update(request):
    credentials_data = Credential.objects.all()
    context = {'credentials_data': credentials_data}
    return render(request, 'mapapp/status_update_views.html', context)'''

  # Make sure to import the model

def status_update(request):
    credentials_data = Credential.objects.all()
    context = {'credentials_data': credentials_data}
    return render(request, 'mapapp/status_update_view.html', context)



@api_view(['GET'])
def credential_list(request):
    credentials = Credential.objects.all()
    serializer = CredentialSerializer(credentials, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def approved_users(request):
    try:
        approved_users = Credential.objects.filter(latitude__isnull=False, longitude__isnull=False)
        serializer = CredentialSerializer(approved_users, many=True)

        markers = [
            {
                'latitude': user_data['latitude'],
                'longitude': user_data['longitude'],
                'username': user_data['username'],
                'status': user_data['status'],
            }
            for user_data in serializer.data
        ]

        return Response(markers)
    except Exception as e:
        return Response({'error': str(e)})

#@api_view(['GET'])
#def home(request):
#    return render(request, 'mapapp/index.html')

@api_view(['GET'])
def redirect_to_mapapp(request):
    return redirect('mapapp:home')



def create_employee(request):
    # Your view logic here
    return render(request, 'mapapp/create_employee.html')

@api_view(['GET'])
def get_credentials(request):
    data = list(Credential.objects.values('username', 'latitude', 'longitude', 'status'))
    return Response(data)

@api_view(['PUT'])
def update_credential(request, username):
    try:
        credential = Credential.objects.get(username=username)
    except Credential.DoesNotExist:
        return Response({"error": "Credential not found"}, status=404)

    serializer = CredentialSerializer(credential, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Credential updated!"})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def add_credential(request):
    serializer = CredentialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def map_with_markers(request):
    return render(request, 'mapapp/map_with_markers.html')


@api_view(['PUT'])
def status_update_credential(request, username):
    try:
        credential = Credential.objects.get(username=username)
    except Credential.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Use the correct serializer
    serializer = StatusUpdateSerializer(credential, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def incidents_view(request):
    return render(request, 'mapapp/incident.html')



def report_incident(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to a new URL or show a success message
            return redirect('some_success_url')
    else:
        form = IncidentReportForm()

    context = {
        'form': form,
    }
    return render(request, 'incidents.html', context)

#patron Side

@api_view(['PUT'])
@permission_classes([IsAuthenticated])  # Only authenticated users can update incidents
def update_incident(request, incident_number):
    try:
        incident = Incidents.objects.get(incident_number=incident_number)
    except Incidents.DoesNotExist:
        return Response({"error": "Incident not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = IncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Help on the way start code


@api_view(['GET', 'PUT'])
@parser_classes([JSONParser])
def manage_need_help(request, username):
    try:
        instance = needHelp.objects.get(username=username)
    except needHelp.DoesNotExist:
        instance = None

    if request.method == "PUT":
        if instance:
            serializer = NeedHelpSerializer(instance, data=request.data)
        else:
            serializer = NeedHelpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        if instance:
            serializer = NeedHelpSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"error": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST'])  # Example permission, requires authenticated user
def need_help_list_create(request):
    if request.method == 'GET':
        queryset = needHelp.objects.all()
        serializer = NeedHelpSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = NeedHelpSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            try:
                instance = needHelp.objects.get(username=username)
                for key, value in serializer.validated_data.items():
                    setattr(instance, key, value)
                instance.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except needHelp.DoesNotExist:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#incident form


def incident_report(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mapapp/home.html')  # replace with your success URL
    else:
        form = IncidentReportForm()
        messages.success(request, 'there was an error processing the form ')
    return render(request, 'mapapp/incident_report.html', {'form': form})



'''def credential_count(request):
    total_responders = Credential.objects.all().count()
    context = {'total_responders': total_responders}
    return render(request, 'mapapp/home.html', context)'''
#messaging framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer
from django.shortcuts import render




class SendMessageAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#ef msg_txt(request):
#    users = Credential.objects.all()
#    return render(request, 'msg_txt.html', {'users': users})




def message_board(request):
    users = Credential.objects.all()
    print(users)
    return render(request, 'mapapp/message_board.html', {'users': users})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message, Credential
from .serializers import MessageSerializer


class ReceiveMessageAPI(APIView):

    def post(self, request):
        sender_username = request.data.get('sender')

        # Get the sender Credential object
        try:
            sender_credential = Credential.objects.get(username=sender_username)
        except Credential.DoesNotExist:
            return Response({"error": "Sender not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Get the Command Post Credential object for the receiver
        try:
            receiver_credential = Credential.objects.get(username='Command Post')
        except Credential.DoesNotExist:
            return Response({"error": "Receiver (Command Post) not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare the data for serialization
        data = {
            'sender': sender_credential.id,
            'receiver': receiver_credential.id,
            'message_text': request.data.get('message_text')
        }

        serializer = MessageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def rec_msg(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({"error": "only POST method allowed"}, status=400)

