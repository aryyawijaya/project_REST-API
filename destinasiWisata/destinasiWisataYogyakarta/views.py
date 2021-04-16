from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from destinasiWisataYogyakarta.models import Destination
from destinasiWisataYogyakarta.serializers import DestinationSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Create your views here.


class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

# @api_view(['GET', 'POST'])
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get(self, request):
    #     if request.method == 'GET':
    #         queryset = User.objects.all()
    #         serializer = UserSerializer(queryset, many=True)
    #         return Response(serializer.data)
    #     elif request.method == 'POST':
    #         serializer = UserSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)

# class UserPOST()
    
# class UserViewSet(APIView):            
#     def get(self, request, pk=None, format=None):
#         user = ...    
#         serializer_context = {
#             'request': request,
#         }
#         serializer = UserSerializer(user, context=serializer_context)    
#         return Response(serializer.data)

    # def list(self, request, format=None):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

# @csrf_exempt
# def destinasiWisataYogyakarta_detail(request, pk):
#     try:
#         destination = Destination.objects.get(pk=pk)
#     except Destination.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = DestinationSerializer(destination)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = DestinationSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         destination.delete()
#         return HttpResponse(status=204)