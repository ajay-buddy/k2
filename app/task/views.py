from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Task
from .serializer import TaskSerializer

# Create your views here.


class TaskAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []

    queryset               = Task.objects.all()
    serializer_class       = TaskSerializer