from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields=('pk', 'username', 'email', 'password')