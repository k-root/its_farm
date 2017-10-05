# -*- coding: utf-7 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Farmer(models.Model):
	Name=models.CharField(max_length=50)
	Gender=models.CharField(max_length=15)
	Age=models.IntegerField()

	def __str__(self):
		reurn self.Name


class Member(models.Model):
	F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)
	Name=models.CharField(max_length=50)
	Gender=models.CharField(max_length=15)
	Age=models.IntegerField()
	Relation=models.CharField(max_length=20, default='')

	def __str__(self):
		return self.Name

class HouseHold(models.Model):
	F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)
	Lat=models.CharField(max_length=15)
	Lon=models.CharField(max_length=15)
	Income=models.IntegerField()

	def __str__(self):
		return self.F_id.Name

class Farm(models.Model):
        F_id=models.ForeignKey(Farmer,on_delete=models.CASCADE)
        Income=models.IntegerField()
        def __str__(self):
                return self.F_id.Name+str(self.id)

class Well(models.Model):
	Farm_id=models.ForeignKey(Farm,on_delete=models.CASCADE)
	Lan=models.FloatField()
	Lon=models.FloatField()
	Depth=models.FloatField()
	Status=models.BooleanField()
	def __str__(self):
		return str(self.id)

class Farmpoints(models.Model):
	Farm_id=models.ForeignKey(Farm,on_delete=models.CASCADE)
	Number=models.IntegerField()
	Lat=models.FloatField()
	Lon=models.FloatField()
	def __str__(self):
		return str(self.id)+self.Farm_id.F_id.Name+str(self.Number)

class Cropping(models.Model):
	Farm_id=models.ForeignKey(Farm,on_delete=models.CASCADE)
	Season=models.CharField(max_length=10)
	Area=models.FloatField()
	Crop=models.CharField(max_length=20)
	def __str__(self):
		return self.Farm_id.F_id.Name + str(self.id)
