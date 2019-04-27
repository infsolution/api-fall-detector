from rest_framework import generics, exceptions
from rest_framework.response import Response
from django.shortcuts import render
from api.models import *
from .serializers import *

class PositionEstateList(generics.ListCreateAPIView):
	queryset = PositionEstate.objects.all()
	serializer_class = PositionEstateSerializer
	name='positionestate-list'

class PositionEstateDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = PositionEstate.objects.all()
	serializer_class = PositionEstateSerializer
	name='positionestate-detail'