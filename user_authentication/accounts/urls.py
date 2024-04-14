from django.urls import path, include
from rest_framework import routers
from accounts.views import UserViewSets, UserLoginView

router = routers.DefaultRouter()
router.register("", UserViewSets, basename="accounts-api")

urlpatterns = [
    path('accounts/', include(router.urls)),
    path('login/', UserLoginView.as_view(), name="login-api"),
]
