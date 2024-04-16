from django.urls import path
from accounts.views import RegisterUserView, VerifyUserEmail, LoginUserView, PasswordResetRequestView, PasswordResetConfirmView, SetNewPasswordView, LogoutUserView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register-api"),
    path('verify-email/', VerifyUserEmail.as_view(), name="verify-email-api"),
    path('login/', LoginUserView.as_view(), name="login-api"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh-api"),
    path('password-reset/', PasswordResetRequestView.as_view(), name="password-reset"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password-reset-confirm-api"),
    path('set-new-password/', SetNewPasswordView.as_view(), name="set-new-password-api"),
    path('logout/', LogoutUserView.as_view(), name="logout-api"),
]
