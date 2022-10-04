from .models import Info
from rest_framework import serializers

class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info

        fields = ['transaction','date','value','cpf','card','hour','owner','store']

        def create(self, validated_data):
           
            info = Info.objects.create(**validated_data)
            return info
