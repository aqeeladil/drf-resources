from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from .throttles import RandomRateThrottle, BurstRateThrottle, SustainedRateThrottle

class AnonymousView(APIView):
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        return Response({"message": "Hello Anonymous!"})
    

class UserView(APIView):
    throttle_classes = [BurstRateThrottle, SustainedRateThrottle]

    def get(self, request):
        return Response({"message": "Hello Authenticated User!"})
    

class ContactView(APIView):
    throttle_scope = 'contacts'

    def get(self, request):
        return Response({"message": "Contact info access!"})


class UploadView(APIView):
    throttle_scope = 'uploads'

    def post(self, request):
        return Response({"message": "Upload successful!"})
    

class RandomThrottleView(APIView):
    throttle_classes = [RandomRateThrottle]

    def get(self, request):
        return Response({"message": "You passed the random throttle!"})