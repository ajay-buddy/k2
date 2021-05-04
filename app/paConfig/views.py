import json
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from paConfig.models import ClientBinding,FeaturesBinding,MatrixBinding

class FetchClientsApiView(APIView):
    permission_classes     = []
    authentication_classes = []
    def get(self, request, format=None):
        clients = [{
            "label": "client1",
            "value": "ac836a33-f40b-4e6a-942d-0cf35083bdeb"
        },{
            "label": "client2",
            "value": "83363026-a3c6-463c-8ebe-16d4a8a64410"
        },{
            "label": "client3",
            "value": "2c06b165-cabb-4758-893e-829359a6807e"
        },{
            "label": "client4",
            "value": "b1d59edf-d6f3-4c55-8570-e5a29513806f"
        }]
        print(clients)
        return Response(status=200, data=clients)

class FetchStudyGroupApiView(APIView):
    permission_classes     = []
    authentication_classes = []
    def get(self, request, format=None):
        study_group = [{
            "label": "study_group1",
            "value": "25f2e2f3-3d2a-4999-a827-be8e5d6c5265"
        },{
            "label": "study_group2",
            "value": "494f20df-0723-45b9-aad2-3adcb46e04ed"
        },{
            "label": "study_group3",
            "value": "14bff409-af56-471a-8c03-9a59f74a64c2"
        },{
            "label": "study_group4",
            "value": "3b586a49-c731-49c6-9bd6-31682bed4898"
        }]
        return Response(status=200, data=study_group)

class ClientBindingsAPIView(APIView):
    permission_classes     = []
    authentication_classes = []
    def post(self, request, format=None):

        client          = request.data.get("client")
        study_group     = request.data.get("study_group")
        found           = ClientBinding.objects.all().filter(client=client)
        if len(found) > 0:
            item = found[0]
            item.study_group = study_group
            item.save()
        else:
            client_binding = ClientBinding(client=client, study_group=study_group)
            client_binding.save()
        return Response(status=201)
    def get(self, request, format=None):
        
        try:
            client = request.GET["client_id"]
            found  = ClientBinding.objects.all().filter(client=client)[0]
            print(found)
            return Response(status=200,data=json.loads(serializers.serialize('json', [found])))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class FeaturesBindingAPIView(APIView):
    permission_classes     = []
    authentication_classes = []
    def post(self, request, format=None):

        client          = request.data.get("client")
        forecast        = request.data.get("forecast")
        reforecast      = request.data.get("reforecast")
        portfolioView   = request.data.get("portfolioView")
        found           = FeaturesBinding.objects.all().filter(client=client)
        if len(found) > 0:
            item = found[0]
            item.forecast = forecast
            item.reforecast = reforecast
            item.portfolioView = portfolioView
            item.save()
        else:
            client_binding = FeaturesBinding(
                client=client, 
                forecast=forecast,
                reforecast=reforecast,
                portfolioView=portfolioView
                )
            client_binding.save()
        return Response(status=201)
    def get(self, request, format=None):
        
        try:
            client = request.GET["client_id"]
            found  = FeaturesBinding.objects.all().filter(client=client)[0]
            print(found)
            return Response(status=200,data=json.loads(serializers.serialize('json', [found])))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MatrixBindingAPIView(APIView):
    permission_classes     = []
    authentication_classes = []
    def post(self, request, format=None):

        client = request.data.get("client")
        ctms_matrix                 = request.data.get("ctms_matrix")
        design_optimization_matrix  = request.data.get("design_optimization_matrix")
        cost_matrix                 = request.data.get("cost_matrix")
        found                       = MatrixBinding.objects.all().filter(client=client)
        if len(found) > 0:
            item = found[0]
            item.ctms_matrix = ctms_matrix
            item.design_optimization_matrix = design_optimization_matrix
            item.cost_matrix = cost_matrix
            item.save()
        else:
            client_binding = MatrixBinding(
                client=client, 
                ctms_matrix=ctms_matrix,
                design_optimization_matrix=design_optimization_matrix,
                cost_matrix=cost_matrix
                )
            client_binding.save()
        return Response(status=201)
    
    def get(self, request, format=None):
        
        try:
            client = request.GET["client_id"]
            found  = MatrixBinding.objects.all().filter(client=client)[0]
            print(found)
            return Response(status=200,data=json.loads(serializers.serialize('json', [found])))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    