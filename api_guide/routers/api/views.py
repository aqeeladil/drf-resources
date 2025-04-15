from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        return Response({'message': f"Password changed for user {pk}"})

class ReportViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({'reports': ['Report A', 'Report B']})

class ForgotPasswordFormView(APIView):
    def get(self, request):
        return Response({'form': 'This would be a password reset form.'})
