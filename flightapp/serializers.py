from rest_framework import serializers
from .models import Flight,Passenger,Reservation
import re

#There are three ways to validdate a data

#1,Rarely used and data contains all the fields values
def isvlaidflightnumber(data):
    print(data)
    return data


class Reservationserializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'
           
class Flightserializer(serializers.ModelSerializer):
    passengers=Reservationserializer(read_only=True,many=True)
    class Meta:
        model=Flight
        fields='__all__'
        validators=[isvlaidflightnumber]    #This is for the outside declared validation function

    #2,To declatre validations for a sepcific attribute
    def validate_flightNumber(self,flightNumber):
        if(re.match("^[a-zA-Z0-9]*$",flightNumber)==None):
            raise serializers.ValidationError("Invalid Flight Number")
        return flightNumber

    #3,To declare a validations generally and here data also contains entire record as a dictionary
    def validate(self,data):
        print(data['flightNumber'])
        return data

class Passengerserializer(serializers.ModelSerializer):
    flights=Reservationserializer(read_only=True,many=True)
    class Meta:
        model=Passenger
        fields='__all__'





