# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
def index(request):
	return HttpResponse('<h3>The index page of App</h3>')

class Wells(APIView):
	def get(self,request):
		welllist = Well.objects.all()
		serializer=WellSerializer(welllist, many=True)
		return Response(serializer.data)
	def post(self,request):
		pass
	

def maps(request):
    #template = loader.get_template('maps/maps.html')
    markers1={0:{'lat':-33.7772, 'long':151.1241}}
    return render(request, 'app/maps.html',{'points':markers1})

class MapList(APIView):
	def get(self, request):
		maplist = Farmpoints.objects.all()
		serializer=FarmpointSerializer(maplist, many=True)
		return Response(serializer.data)
	def post(self):
		pass

#class News(APIView):
#	def get(self,request):
	#	query= Farmpoints.objects.raw('SELECT * FROM Farm JOIN Farmer JOIN Farmpoints WHERE Farmpoints.Farm_id= 1')
#		return render(request, 'app/maps.html',{'farmdet':query})
#		query=Farmer.objects.raw('SELECT * FROM app_farmer JOIN app_farm ON app_farmer.id=1')
#		return render(request, 'app/abc.html',{'resu':query})


@api_view(['GET', 'PUT', 'DELETE'])
def MapDetail(request,pk, format=None):
	try:
		map_detail=Farmpoints.objects.get(pk=pk)
	except Farmpoints.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='GET':
		serializer=FarmpointSerializer(map_detail)
		return Response(serializer.data)

	elif request.method=='PUT':
		serializer=FarmpointSerializer(map_detail, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method=='DELETE':
		map_detail.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class FarmerList(APIView):
	def get(self,request):
		farmerlist = Farmer.objects.all()
		serializer=FarmerSerializer(farmerlist, many=True)
		return Response(serializer.data)
	def post(self,request):
		pass

@api_view(['GET', 'PUT', 'DELETE'])
def FarmerDetail(request,pk, format=None):
	try:
		f_detail=Farmer.objects.get(pk=pk)
	except Farmer.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='GET':
		serializer=FarmerSerializer(f_detail)
		return Response(serializer.data)

	elif request.method=='PUT':
		serializer=FarmerSerializer(f_detail, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method=='DELETE':
		f_detail.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class HouseHoldList(APIView):
	def get(self, request):
		hhlist = HouseHold.objects.all()
		serializer=HouseHoldSerializer(hhlist, many=True)
		return JsonResponse(serializer.data, safe=False)
	def post(self):
		pass
@api_view(['GET', 'PUT', 'DELETE'])
def HouseHoldDetail(request,pk, format=None):
	try:
		hh_detail=HouseHold.objects.get(pk=pk)
	except HouseHold.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='GET':
		serializer=HouseHoldSerializer(hh_detail)
		return Response(serializer.data)

	elif request.method=='PUT':
		serializer=HouseHoldSerializer(hh_detail, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method=='DELETE':
		hh_detail.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class MemberList(APIView):
	def get(self, request):
		memberlist = Member.objects.all()
		serializer=MemberSerializer(memberlist, many=True)
		return Response(serializer.data)
	def post(self):
		pass
@api_view(['GET', 'PUT', 'DELETE'])
def MemberDetail(request,pk, format=None):
	try:
		m_detail=Member.objects.get(pk=pk)
	except Member.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='GET':
		serializer=MemberSerializer(m_detail)
		return Response(serializer.data)

	elif request.method=='PUT':
		serializer=MemberSerializer(m_detail, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method=='DELETE':
		m_detail.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class FarmList(APIView):
        def get(self, request):
                flist = Farm.objects.all()
                serializer=FarmSerializer(flist, many=True)
                return Response(serializer.data)
        def post(self):
                pass

