from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RestaurantSerializer,RegisterSerializer,UserSerializer,RezervacijaSerializer
from base.models import Restaurants,Rezervacija
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated


@api_view(['GET'])
def getData(request):
    rest = Restaurants.objects.all()
    serializer = RestaurantSerializer(rest,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
    user = User.objects.all()
    serializer = UserSerializer(user,many=True)
    return Response (serializer.data)




class GetRestaurants(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        
        queryset = Restaurants.objects.all()    
        serializer = RestaurantSerializer(queryset,many=True)  
        return Response({"data":serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRestaurant(request):
    data = request.data
    data['vlasnik'] = request.user.id
    serializer = RestaurantSerializer(data=data,partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class GetMyRestaurants(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        queryset = Restaurants.objects.filter(vlasnik=request.user.id)
        serializer = RestaurantSerializer(queryset,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRez(request):
    serializer = RezervacijaSerializer(data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)

class GetRez(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        queryset = Rezervacija.objects.filter(restoran=request.data["restoran"])
        serializer = RezervacijaSerializer(queryset,many=True)
        return Response(serializer.data)
