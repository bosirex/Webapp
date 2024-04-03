from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import SimpleMessage
from .serializers import SimpleMessageSerializer
from django.shortcuts import redirect
from django.views import View

@api_view(['GET', 'POST'])
def message_list(request):
    if request.method == 'GET':
        messages = SimpleMessage.objects.all()
        serializer = SimpleMessageSerializer(messages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SimpleMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendMessageView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('logged_in_users')
        message_content = request.POST.get('message_input')

        if username and message_content:
            SimpleMessage.objects.create(username=username, message=message_content)

        return redirect('home')
  # replace with your home view's name
