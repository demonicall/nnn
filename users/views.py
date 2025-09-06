from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema, OpenApiExample

from .pagination import CustomPagination
from .serializers import UsersSerializer

@extend_schema(
    tags=["Auth"],
    request=UsersSerializer,
    examples=[
        OpenApiExample(
            "Register Example",
            value={
                "username": "string",
                "email": "email",
                "password": "string"
            },
        ),
    ],
)
@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register_view(request):
    serializer = UsersSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = serializer.save()
    refresh = RefreshToken.for_user(user)

    response = Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    response.set_cookie("access_token", str(refresh.access_token), httponly=True, secure=False, samesite="Lax")
    response.set_cookie("refresh_token", str(refresh), httponly=True, secure=False, samesite="Lax")
    return response

@extend_schema(tags=["Auth"])
class CookieLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

@extend_schema(tags=["Auth"])
@api_view(["POST"])
def logout_view(request):
    response = Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response

@extend_schema(tags=["Users"])
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes(permissions.AllowAny)
    search_fields = ["username"]
    pagination_class = CustomPagination

@extend_schema(tags=["Users"])
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]


