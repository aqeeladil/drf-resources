import random
from rest_framework.throttling import BaseThrottle, UserRateThrottle

class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'

class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'

class RandomRateThrottle(BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1  # 90% chance to pass

    def wait(self):
         # This would return the number of seconds a client should wait before retrying
        return 5     # if the request is denied, wait for 5 seconds before retrying
    
    
