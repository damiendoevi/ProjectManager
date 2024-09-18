from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsNotAuthenticated
from rest_framework.request import Request

from drf_spectacular.utils import extend_schema, OpenApiResponse
from .throttles import CustomUserRateThrottle

# Create your views here.


class DestroyTokenView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [CustomUserRateThrottle]

    @extend_schema(
        request=None,
        responses={
            200: OpenApiResponse(description='Token destroyed successfully'),
            400: OpenApiResponse(description='Bad request'),
        }
    )
    def post(self, request):
        response = Response(status=status.HTTP_200_OK)

        refresh_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_REFRESH_COOKIE']) or None

        if refresh_token:

            try:
                refresh_token = RefreshToken(refresh_token)
                refresh_token.blacklist()

            except TokenError:
                access_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
                access_token = RefreshToken(access_token)
                refresh_token.blacklist()

            response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
            response.delete_cookie(settings.SIMPLE_JWT['AUTH_REFRESH_COOKIE'])

            return response
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
            

class MyTokenObtainPairView(TokenObtainPairView):
    throttle_classes = [CustomUserRateThrottle]
    permission_classes = [IsNotAuthenticated]

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        response = Response()

        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
            value = serializer.validated_data.get("access"),
            domain=settings.SIMPLE_JWT["COOKIE_DOMAIN"],
            expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure = settings.SIMPLE_JWT['COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['COOKIE_SAMESITE']
        )

        response.set_cookie(
            key = settings.SIMPLE_JWT['AUTH_REFRESH_COOKIE'], 
            value = serializer.validated_data.get("refresh"),
            domain=settings.SIMPLE_JWT["COOKIE_DOMAIN"],
            expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure = settings.SIMPLE_JWT['COOKIE_SECURE'],
            httponly = settings.SIMPLE_JWT['COOKIE_HTTP_ONLY'],
            samesite = settings.SIMPLE_JWT['COOKIE_SAMESITE']
        )

        response.data = serializer.validated_data
        response.status_code = status.HTTP_200_OK

        return response;