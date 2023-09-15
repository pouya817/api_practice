from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
# Create your views here.

class helloapi(APIView):
    

    serializer_class = serializers.helloserializer

    def get(self,request , format = None):
        an_apiview=[
            'wellcome'
        ]
        return Response({'message':'hello!', 'an_apiview': an_apiview})
    
    def post (self, request):
        serializer =serializers.helloserializer(data=request.data)

        if serializer.is_valid():
            name= serializer.data.get('name')
            message = "hello {0}".format(name)
            return Response({"message":message})
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        