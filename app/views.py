# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

def index(request):
	return HttpResponse('<h3>The index page of App</h3>')

class FarmerList(APIView):
	def get(self,request):
		farmerlist = Farmer.objects.all()
		serializer=FarmerSerializer(farmerlist, many=True)
		return Response(serializer.data)
	def post(self,request):
		pass

class HouseHoldList(APIView):
	def get(self, request):
		hhlist = HouseHold.objects.all()
		serializer=HouseHoldSerializer(hhlist, many=True)
		return Response(serializer.data)
	def post(self):
		pass

class MemberList(APIView):
	def get(self, request):
		memberlist = Member.objects.all()
		serializer=MemberSerializer(memberlist, many=True)
		return Response(serializer.data)
	def post(self):
		pass