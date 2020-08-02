from .models import Carrot
from rest_framework import serializers

class CarrotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrot
        fields = ('time', 'temperature', 'wetness', 'HP', 'award', 'end_status')

class CarrotRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrot
        fields = ('time', 'temperature', 'wetness', 'HP', 'award', 'end_status')

class CarrotWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrot
        fields = ('time', 'temperature', 'wetness', 'HP', 'award', 'end_status')
