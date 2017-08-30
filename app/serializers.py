from rest_framework import serializers
from .models import *

class FarmerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Farmer
		fields='__all__'

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model=Member 
		fields='__all__'

class HouseHoldSerializer(serializers.ModelSerializer):
	class Meta:
		model=HouseHold
		fields='__all__'