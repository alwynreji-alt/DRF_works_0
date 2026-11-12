from dataclasses import dataclass

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import employee
from .serializers import EmployeeSerializer
from django.http import JsonResponse


class employeelist(APIView):
    def get(self,request):
        data=employee.objects.all() #query set
        serializer_inst=EmployeeSerializer(data,many=True)#query to pyth_native
        print(serializer_inst)
        return Response(serializer_inst.data) #return response

class employeecreate(APIView):
    def post(self,request):
        serializer_inst = EmployeeSerializer(data=request.data)
        print(request.data)
        if serializer_inst.is_valid():
            serializer_inst.save()
            return Response({"message ":"created"})
        else:
            return Response(serializer_inst.errors)

class employeedetail(APIView):
    def get(self,request,i):
        w=get_object_or_404(employee,id=i)
        serializers_inst=EmployeeSerializer(w)
        return Response(serializers_inst.data)

class employeedelete(APIView):
    def delete(self,request,i):
        q=get_object_or_404(employee,id=i)
        q.delete()
        return Response({"message ": "Record has been Deleted"})

class employeeupdate(APIView):
    def put(self,request,i):
        q=get_object_or_404(employee,id=i)
        data=request.data
        serializers_inst=EmployeeSerializer(instance=q,data=data)
        if serializers_inst.is_valid():
            serializers_inst.save()
            return Response(serializers_inst.data)
        else:
            return Response(serializers_inst.errors)

class employeepartialupdate(APIView):
    def patch(self,request,i):
        q=get_object_or_404(employee,id=i)
        data=request.data
        serializers_inst=EmployeeSerializer(instance=q,partial=True,data=data)
        if serializers_inst.is_valid():
            serializers_inst.save()
            return Response(serializers_inst.data)
        else:
            return Response(serializers_inst.errors)

