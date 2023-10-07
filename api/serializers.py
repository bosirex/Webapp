from rest_framework import serializers
from mapapp.models import Credential,Incidents

class CredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['id', 'username', 'password', 'latitude', 'longitude', 'acceleration', 'status', 'timestamp']

class DeviceLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['username', 'password']




class StatusUpdateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['status']
# patron side
