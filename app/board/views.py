from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Board
from .serializer import BoardSerializer

# Create your views here.


class BoardAPIView(generics.ListAPIView, generics.CreateAPIView):
    permission_classes     = []
    authentication_classes = []

    queryset               = Board.objects.all()
    serializer_class       = BoardSerializer