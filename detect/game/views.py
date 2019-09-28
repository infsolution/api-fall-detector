from rest_framework import generics, exceptions
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import *
from .models import *
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserCreateSerializer
	name='user-list'
	def perform_create(self, serializer):
		user=User.objects.create_user(serializer.data['username'], serializer.data['email'], serializer.data['password'])
		print(serializer.data['username'])
		serializer.data['pk']=user.id
		return Response(serializer.data)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserCreateSerializer
	name='user-detail'
