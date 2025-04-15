from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ReportViewSet
from django.urls import path
from .views import ForgotPasswordFormView

router = SimpleRouter(trailing_slash=False)  # no trailing slash

router.register(r'users', UserViewSet)
router.register(r'reports', ReportViewSet, basename='report')

urlpatterns = [
    path('forgot-password', ForgotPasswordFormView.as_view())
]

urlpatterns += router.urls
