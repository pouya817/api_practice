from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class helloapi(APIView):

    def get(self,request , format = None):
        an_apiview=[
            'wellcome'
        ]
        return Response({'message':'hello!', 'an_apiview': an_apiview})