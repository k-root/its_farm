# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Farmer(models.Model):
	Name=models.CharField(max_length=50)
	Gender=models.CharField(max_length=15)
	Age=models.IntegerField()

	def __str__(self):
		return self.Name


class Member(models.Model):
	F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)
	Name=models.CharField(max_length=50)
	Gender=models.CharField(max_length=15)
	Age=models.IntegerField()
	Relation=models.CharField(max_length=15, default='')

	def __str__(self):
		return self.Name


class HouseHold(models.Model):
	F_id=models.ForeignKey(Farmer, on_delete=models.CASCADE)
	Lat=models.CharField(max_length=15)
	Lon=models.CharField(max_length=15)
	Income=models.IntegerField()

	def __str__(self):
		return self.F_id.Name