from django.urls import path
from authorization.views import SignInView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', SignInView.as_view(), name='user_signin'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='user_register'),
]