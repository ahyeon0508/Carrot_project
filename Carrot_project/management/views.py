from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Carrot
from .serializers import CarrotSerializer, CarrotRetrieveSerializer, CarrotWriteSerializer

class Carrot_status_list(ListAPIView):
    queryset = Carrot.objects.all()
    serializer_class = CarrotSerializer

class Carrot_status_retrieve(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Carrot.objects.all().order_by('-time')
    serializer_class = CarrotRetrieveSerializer

class Carrot_status_update(UpdateAPIView):
    queryset = Carrot.objects.all()
    serializer_class = CarrotSerializer

class Carrot_status_delete(DestroyAPIView):
    queryset = Carrot.objects.all()
    serializer_class = CarrotSerializer

class Carrot_status_write(CreateAPIView):
    queryset = Carrot.objects.all()
    serializer_class = CarrotWriteSerializer

class CurrentCarrotStatus(APIView):
    def get(self, request):
        serializer = CarrotSerializer(Carrot.objects.all().order_by('-time')[0])
        return Response(serializer.data)

