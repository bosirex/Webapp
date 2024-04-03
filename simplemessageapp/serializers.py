from rest_framework import serializers
from .models import SimpleMessage

class SimpleMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleMessage
        fields = ['username', 'message']
