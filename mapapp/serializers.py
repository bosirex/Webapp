from rest_framework.serializers import ModelSerializer
from .models import Credential, Incidents, needHelp, Message  # Ensure Message is imported here

class CredentialSerializer(ModelSerializer):
    class Meta:
        model = Credential
        fields = '__all__'

class StatusUpdateSerializer(ModelSerializer):
    class Meta:
        model = Credential
        fields = ['status']

class IncidentSerializer(ModelSerializer):
    class Meta:
        model = Incidents
        fields = '__all__'

class NeedHelpSerializer(ModelSerializer):
    class Meta:
        model = needHelp
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message_text']
