from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from inventory.models import Vehicle, Booking
from inventory.serialzer import Vehicleserialzer , Bookingserialzer

class Vehiclelist(APIView):
    def get(self,request):

        v = Vehicle.objects.all()
        s = Vehicleserialzer(v , many=True)
        return Response(s.data , status=status.HTTP_200_OK)

    def post(self,request):

        k = Vehicleserialzer(data=request.data)

        if k.is_valid():
            k.save()
            return Response(k.data , status=status.HTTP_201_CREATED)

class Vehicledetails(APIView):
    def get(self,request , id):

        try:
            l = Vehicle.objects.get(id=id)
        except:
            return Response ({"This Vehicle is not Found"}, status=status.HTTP_404_NOT_FOUND)

        p = Vehicleserialzer(l)
        return Response(p.data)

    def Put(self,request , id):

        try:
            v = Vehicle.objects.get(id=id)
        except:
            return Response ({"This Vehicle is not Found"}, status=status.HTTP_404_NOT_FOUND)

        t = Vehicleserialzer(v , data=request.data)

        if t.is_valid():
            t.save()

            return Response(t.data)

    def delete(self,request, id):

        try:
            y = Vehicle.objects.get(id=id)
        except:
            return Response({"This vehicle is not found"},status=status.HTTP_404_NOT_FOUND)

        y.delete()

        return Response({"Vehicle deleted"}, status=status.HTTP_200_OK)


class Bookinglist(APIView):
    def get(self,request):

        b = Booking.objects.all()
        h = Bookingserialzer(b , many=True)

        return Response (h.data , status=status.HTTP_201_CREATED)


    def post(slef,request):

        l = Bookingserialzer(data=request.data)

        if l.is_valid():
            l.save()

            return Response(l.data , status=status.HTTP_201_CREATED)

class Bookingdetails(APIView):
    def get(self,request, id):
        

        b = Booking.objects.get(id=id)

        f = Bookingserialzer(b)

        return Response(f.data)

    def delete(self,request , id):

        try:
            l = Booking.objects.get(id=id)
        except:

            return Response({"This user is not exist"},status=status.HTTP_404_NOT_FOUND)

        l.delete()
        return Response({"The Booking is deleted"})


    




        
    