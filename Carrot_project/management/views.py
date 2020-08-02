from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from .models import Carrot
from .serializers import CarrotSerializer, CarrotRetrieveSerializer, CarrotWriteSerializer

class Carrot_status_list(ListAPIView):
    queryset = Carrot.objects.all()
    serializer_class = CarrotSerializer

class Carrot_status_retrieve(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Carrot.objects.all()
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

class CurrentCarrotStatus(ListAPIView):
    queryset = Carrot.objects.all().order_by('-time')[:1]
    serializer_class = CarrotSerializer

# def getFeedback(self, request):

