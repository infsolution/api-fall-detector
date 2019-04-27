from rest_framework import serializers
from .models import *
class PositionEstateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PositionEstate
		fields = ('url','pk', 'posX','posY','posZ','acelX','acelY','acelZ')