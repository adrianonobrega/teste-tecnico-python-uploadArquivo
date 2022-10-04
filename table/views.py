from django.shortcuts import render
from rest_framework import generics
from .models import Txt
from .serializers import UploadSerializer

# Create your views here.

class Upload(generics.CreateAPIView):
    serializer_class = UploadSerializer