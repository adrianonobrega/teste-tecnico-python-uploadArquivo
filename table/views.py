from rest_framework import generics
from .serializers import UploadSerializer

# Create your views here.

class Upload(generics.CreateAPIView):
    serializer_class = UploadSerializer