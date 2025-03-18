from rest_framework import serializers
from .models import Company, Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'

        
    