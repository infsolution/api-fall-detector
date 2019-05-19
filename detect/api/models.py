from django.contrib.auth.models import User
from django.db import models


class Device(models.Model):
	code = models.IntegerField(default=0)
	owner = models.OneToOneField('auth.User', related_name='owner', on_delete=models.CASCADE)
	def __str__(self):
		return str(self.code) 

class PositionEstate(models.Model):
	device = models.ForeignKey(Device, related_name='position', on_delete=models.CASCADE)
	posX = models.DecimalField(max_digits=5, decimal_places=2)
	posY = models.DecimalField(max_digits=5, decimal_places=2)
	posZ = models.DecimalField(max_digits=5, decimal_places=2)
	acelX = models.DecimalField(max_digits=5, decimal_places=2)
	acelY = models.DecimalField(max_digits=5, decimal_places=2)
	acelZ = models.DecimalField(max_digits=5, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = (-id)

