from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import KInstance
from .serializer import KInstanceSerializer
# Create your views here.

class KInstanceAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []

    queryset               = KInstance.objects.all()
    serializer_class       = KInstanceSerializer
