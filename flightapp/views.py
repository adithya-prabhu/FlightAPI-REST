from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .models import Flight,Passenger,Reservation
from .serializers import Flightserializer,Passengerserializer,Reservationserializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
def find_flights(request):
    flights=Flight.objects.filter(departurecity=request.data['departurecity'],arrivalcity=request.data['arrivalcity'],dateofdeparture=request.data['dateofdeparture'])
    ser=Flightserializer(flights,many=True)
    return Response(ser.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_reservation(request):
    flight=Flight.objects.get(id=request.data['flightid'])

    passenger=Passenger()
    passenger.firstName=request.data['firstName']
    passenger.lastName=request.data['lastName']
    passenger.middleName=request.data['middleName']
    passenger.email=request.data['email']
    passenger.phone=request.data['phone']
    passenger.save()

    res=Reservation()
    res.flight=flight
    res.passenger=passenger
    res.save() 
    return Response(status=status.HTTP_201_CREATED)
    

class Flightviewset(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=Flightserializer
    permission_classes=[IsAuthenticated]

class Passengerviewset(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=Passengerserializer

class Reservationviewset(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=Reservationserializer