from rest_framework import viewsets
from .serializers import CompanySerializer, EmployeeSerializer
from .models import Company, Employee
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('company_id')
    serializer_class = CompanySerializer

    # Custom action to get all employees of a company
    # URL:/companies/{pk}/employees/ 
    # localhost:8000/api/v1/companies/1/employees/
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company  = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response({'error': 'Company does not exist'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('employee_id')
    serializer_class = EmployeeSerializer