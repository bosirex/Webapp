from rest_framework import serializers
from .models import EPCR

class EPCRSerializer(serializers.ModelSerializer):
    class Meta:
        model = EPCR
        fields = '__all__'

