from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import students
from rest_framework.views import APIView
from . serializers import studentsSerializer
from rest_framework import status

class studentList(APIView):


    def get(self,request):
        student1=students.objects.all()
        serializer=studentsSerializer(student1,many=True)
        return Response(serializer.data)

    def post(self):
        pass


