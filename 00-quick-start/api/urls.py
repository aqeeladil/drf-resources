from django.urls import path, include
from rest_framework import routers
from .views import UserViewset, GroupViewset


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'groups', GroupViewset)

# The API URLs are now determined automatically by the router.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]