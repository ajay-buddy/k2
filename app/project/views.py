from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project
from .serializer import ProjectSerializer
# Create your views here.

class ProjectView(APIView):
    permission_classes     = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Project.objects.all()
        serializer = ProjectSerializer(qs, many=True)
        return Response(qs)

    def post(self, request, format=None):
        pass

class ProjectAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []

    queryset               = Project.objects.all()
    serializer_class       = ProjectSerializer
