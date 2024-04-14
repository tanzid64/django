from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSets

router = routers.DefaultRouter()
router.register("", UserViewSets, basename="accounts-api")

urlpatterns = [
    path('', include(router.urls)),
]
