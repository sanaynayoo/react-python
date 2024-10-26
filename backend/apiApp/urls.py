from django.urls import path,include
from rest_framework import routers
from apiApp.views import PatientViewSet


router = routers.DefaultRouter()
router.register(r'patient',PatientViewSet)

urlpatterns=[
    path('', include('apiApp.urls')),
]