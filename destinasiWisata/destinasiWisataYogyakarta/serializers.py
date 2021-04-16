from rest_framework import serializers
from destinasiWisataYogyakarta.models import Destination
from django.contrib.auth.models import User 

class DestinationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

    # def create(self, validated_data):
    #     return Destination.objeccts.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'