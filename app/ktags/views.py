from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import KTags
from .serializer import KTagsSerializer
# Create your views here.

class KTagsAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []

    queryset               = KTags.objects.all()
    serializer_class       = KTagsSerializer
