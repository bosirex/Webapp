from rest_framework.serializers import ModelSerializer
from .models import Credential, Incidents, needHelp # Ensure Message is imported here
from rest_framework import serializers
from .models import Message

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
        fields = '__all__'  # or specify the fields you want ['field1', 'field2', ...]
