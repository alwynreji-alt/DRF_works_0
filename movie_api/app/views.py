from email import message

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import movie
from .serializers import MovieSerializer
from rest_framework import status


# Create your views here.
class moviecreate(APIView):
    def post(self,request):
        serializer_inst=MovieSerializer(data=request.data)
        if serializer_inst.is_valid():
            serializer_inst.save()
            return Response({"message":"created"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_inst.errors,status=status.HTTP_400_BAD_REQUEST)

class movielist(APIView):
    def get(self,request):
        data=movie.objects.all()
        serializer_inst= MovieSerializer(data,many=True)
        return Response(serializer_inst.data,status=status.HTTP_200_OK)

class movieretrive(APIView):
    def get(self,request,i):
        w=get_object_or_404(movie,id=i)
        serializer_inst=MovieSerializer(w)
        return Response(serializer_inst.data)

class movieupdate(APIView):
    def put(self,request,i):
        q=get_object_or_404(movie,id=i)
        data=request.data
        serializer_inst=MovieSerializer(instance=q,data=data)
        if serializer_inst.is_valid():
            serializer_inst.save()
            return Response(serializer_inst.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_inst.errors,status=status.HTTP_400_BAD_REQUEST)

class moviepartailupdate(APIView):
    def patch(self,request,i):
        q=get_object_or_404(movie,id=i)
        data=request.data
        serializer_inst=MovieSerializer(instance=q,partial=True,data=data)
        if serializer_inst.is_valid():
            serializer_inst.save()
            return Response(serializer_inst.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_inst.errors,status=status.HTTP_400_BAD_REQUEST)

class moviedelete(APIView):
    def delete(self,request,i):
        q=get_object_or_404(movie,id=i)
        q.delete()
        return Response({"message ": "Record has been Deleted"},status=status.HTTP_204_NO_CONTENT)