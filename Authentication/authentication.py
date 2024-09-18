from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.translation import gettext_lazy as _
from typing import TypeVar
from django.contrib.auth.models import AbstractBaseUser
from rest_framework_simplejwt.models import TokenUser

from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings


AuthUser = TypeVar("AuthUser", AbstractBaseUser, TokenUser)

class CustomJWTAuthentication(JWTAuthentication):
        
    def authenticate(self, request):
        header = self.get_header(request)
        raw_token = None

        if header is None:
            # Check for token in cookies
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
        else:
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None
    
        try:
                validated_token = self.get_validated_token(raw_token)
        except:
            # Check for refresh token in cookies
            raw_refresh_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_REFRESH_COOKIE'])
            if raw_refresh_token:
                try:
                    refresh_token = RefreshToken(raw_refresh_token)
                    new_raw_token = str(refresh_token.access_token)
                    validated_token = self.get_validated_token(new_raw_token)
                except TokenError:
                    return None
                # Return the new token along with the user
                return self.get_user(validated_token), validated_token
            return None

        # Return the validated token along with the user
        return self.get_user(validated_token), validated_token
    

def default_user_authentication_rule(user: AuthUser) -> bool:
    # Prior to Django 1.10, inactive users could be authenticated with the
    # default `ModelBackend`.  As of Django 1.10, the `ModelBackend`
    # prevents inactive users from authenticating.  App designers can still
    # allow inactive users to authenticate by opting for the new
    # `AllowAllUsersModelBackend`.  However, we explicitly prevent inactive
    # users from authenticating to enforce a reasonable policy and provide
    # sensible backwards compatibility with older Django versions.
    return user is not None and user.is_active