from django.urls import path
from social_accounts.views import GoogleSignView

urlpatterns = [
    path('google/', GoogleSignView.as_view(), name='google-signin-api'),
]
