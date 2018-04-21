from django.db import models

class Introduce(models.Model):
	name=models.CharField(max_length=20)
	phone_number=models.CharField(max_length=15)
	address=models.CharField(max_length=50,blank=True)
	def __str__(self):
		return self.name

