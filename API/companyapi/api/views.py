from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
    # URL compies/{companyID}/employees
    @action (detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            companies = get_object_or_404(Company, pk=pk)
            emps=Employee.objects.filter(company=companies)
            emps_serializers=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(  emps_serializers.data)
        except Exception as e:
            return Response({
            'message':e
        })
   
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

