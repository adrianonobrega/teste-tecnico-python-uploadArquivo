from .models import Txt
from rest_framework import serializers

class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Txt

        fields = ['file']