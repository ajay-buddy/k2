from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Space
from .serializer import SpaceSerializer

# Create your views here.


class SpaceAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []

    queryset               = Space.objects.all()
    serializer_class       = SpaceSerializer