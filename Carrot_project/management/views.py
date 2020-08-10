import os
import json

from django.shortcuts import render
from django.core import serializers

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Carrot
from .serializers import CarrotSerializer, CarrotRetrieveSerializer, CarrotWriteSerializer

from .BETA17.AI import get_Action

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

class CarrotCarrotImage(APIView):
    def post(self, request):
        # print("===============")
        # print(os.path.realpath(__file__))
        # print("===============")
        with open('management\static\management\carrot_img.json', 'w', encoding='utf-8') as make_file:
            json.dump(request.data, make_file, indent="\t")
        # carrot_img.write(request.data)
        # carrot_img.close()
        return Response()

    def get(self, request):
        with open('management\static\management\carrot_img.json', 'r') as carrot_img_json:
            carrot_img = json.load(carrot_img_json)
        return Response(carrot_img)

class Carrot_Action(APIView):
    def get(self, request):
        Humid = Carrot.objects.all().order_by('-time')[0].wetness
        Temp = Carrot.objects.all().order_by('-time')[0].temperature
        action = get_Action(Humid, Temp)
        action = {
            'code':action
            }
        return Response(action)






