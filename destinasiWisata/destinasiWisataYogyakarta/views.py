from django.shortcuts import render
from destinasiWisataYogyakarta.models import Destination
from destinasiWisataYogyakarta.serializers import DestinationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# # GET, POST
class DestinationList(APIView):
    # GET
    def get(self, request, format=None):
        destination = Destination.objects.all()
        serializer = DestinationSerializer(destination, many=True)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success get destinations',
                'data': serializer.data
            }
        )
    
    # POST
    def post(self, request, format=None):
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success create new destination',
                    'data': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # GET, PUT, PATCH, DELETE (single model instance)
class DestinationDetail(APIView):
    def get_object(self, pk):
        try:
            return Destination.objects.get(pk=pk)
        except Destination.DoesNotExist:
            raise Http404

    # GET
    def get(self, request, pk, format=None):
        destination = self.get_object(pk)
        serializer = DestinationSerializer(destination)
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success get destination',
                'data': serializer.data
            }
        )

    # PUT
    def put(self, request, pk, format=None):
        destination = self.get_object(pk)
        serializer = DestinationSerializer(destination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success update destination',
                    'data': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH
    def patch(self, request, pk, format=None):
        destination = self.get_object(pk)
        serializer = DestinationSerializer(destination, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_201_CREATED,
                    'message': 'success update some field destination',
                    'data': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    def delete(self, request, pk, format=None):
        destination = self.get_object(pk)
        destination.delete()
        return Response(
            {
                'status': status.HTTP_200_OK,
                'message': 'success delete destination',
                'data': True
            }
        )