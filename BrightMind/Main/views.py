from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Test1(APIView):
    def post(self, request):
        return Response({"message": "First POST method received", "data": request.data}, status=status.HTTP_201_CREATED)

class Test2(APIView):
    def post(self, request):
        return Response({"message": "Second POST method received", "data": request.data}, status=status.HTTP_201_CREATED)
