from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Device
		fields = ('url', 'pk', 'code', 'owner','position')

class PositionEstateSerializer(serializers.HyperlinkedModelSerializer):
	device =  serializers.SlugRelatedField(queryset=Device.objects.all(), slug_field='code')
	class Meta:
		model = PositionEstate
		fields = ('url','pk', 'device','posX','posY','posZ','acelX','acelY','acelZ')

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields=('pk', 'username', 'email', 'password')