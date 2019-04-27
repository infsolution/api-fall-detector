from django.db import models

class PositionEstate(models.Model):
	posX = models.DecimalField(max_digits=5, decimal_places=2)
	posY = models.DecimalField(max_digits=5, decimal_places=2)
	posZ = models.DecimalField(max_digits=5, decimal_places=2)
	acelX = models.DecimalField(max_digits=5, decimal_places=2)
	acelY = models.DecimalField(max_digits=5, decimal_places=2)
	acelZ = models.DecimalField(max_digits=5, decimal_places=2)
