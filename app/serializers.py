from rest_framework import serializers
from .models import *

class FarmpointSerializer(serializers.ModelSerializer):
	class Meta:
		model=Farmpoints
		fields='__all__'

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

class FarmSerializer(serializers.ModelSerializer):
        class Meta:
                model=Farm
                fields='__all__'

class WellSerializer(serializers.ModelSerializer):
	class Meta:
		model=Well
		fields='__all__'

