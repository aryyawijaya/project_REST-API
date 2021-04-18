from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from destinasiWisataYogyakarta.models import Destination
# from django.contrib.auth.models import User
from destinasiWisataYogyakarta.serializers import DestinationSerializer
# from rest_framework import viewsets, mixins, generics
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework import status
from rest_framework import generics
# from django.http import Http404

# Create your views here.

# class DestinationViewSet(viewsets.ModelViewSet):
#     queryset = Destination.objects.all()
#     serializer_class = DestinationSerializer

# GET, POST
class DestinationList(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

# @api_view(['GET', 'POST',])
# def destination_list(request):
#     if request.method == 'GET':
#         destination = Destination.objects.all()
#         serializer = DestinationSerializer(destination, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = DestinationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET, PUT, PATCH, DELETE (single model instance)
class DestinationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

# @api_view(['GET', 'PUT', 'DELETE',])
# def destination_detail(request, pk):
#     try:
#         destination = Destination.objects.get(pk=pk)
#     except Destination.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DestinationSerializer(destination)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = DestinationSerializer(destination, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         destination.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# @api_view(['GET', 'POST',])
# def user_list(request):
#     if request.method == 'GET':
#         user = User.objects.all()
#         serializer = UserSerializer(user, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# @api_view(['GET',])
# def user_detail(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# @api_view(['GET', ])
# def UserViewSet(request, slug):
#     try:
#         user = User.objects.get(slug=slug)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

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