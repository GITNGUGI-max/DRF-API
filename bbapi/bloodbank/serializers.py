from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields= ('url', 'id', 'username', 'password')
	

class CountySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=County
		fields=('url', 'id', 'countyName')

class SubCountySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model=SubCounty
		fields=['url', 'id', 'county', 'subCountyName']	

class DonorSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
	 	model=Donor
fields=['url', 'id', 'donorName', 'gender', 'dateOfBirth', 'bloodGroup', 'weight', 'email', 
	 			'location', 'county', 'subCounty', 'contactOne', 'contactTwo', 'voluntary', 'newDonor', 
	 			'lastDonated', 'image']

	 	
class PatientSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model=Patient
		fields='__all__'
		include='owner'
class MessageSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model=Message
		fields='__all__'




