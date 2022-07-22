from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
# Create your views here.
from .permissions import IsOwnerOrReadOnly
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



# @api_view(['GET'])
# def api_root(request, format=None):
# 	return Response({
# 		'users':reverse('user-list', request=request, format=format),
# 		'donors':reverse('donor-list', request=request, format=format),
# 		'patients':reverse('patient-list', request=request, format=format),
# 		'counties ':reverse('county-list', request=request, format=format),
# 		'messages ':reverse('message-list', request=request, format=format),
# 		'sub_counties':reverse('sub_county-list', request=request, format=format),
# 		})

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer
class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer	  

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer	
class CountyViewSet(viewsets.ModelViewSet):
	queryset=County.objects.all()
	serializer_class=CountySerializer	
class SubCountyViewSet(viewsets.ModelViewSet):
	queryset=SubCounty.objects.all()
	serializer_class=SubCountySerializer	
class MessageViewSet(viewsets.ModelViewSet):
	queryset=Message.objects.all()
	serializer_class=MessageSerializer	
