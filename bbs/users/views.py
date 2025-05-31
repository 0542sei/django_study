from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import Profile

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView): #일반적인 뷰에는 GenericAPIView 사용
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key},status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveUpdateAPIView): #generics를 사용할 때는 querset,serializer_class만 잘 지정해주면 됨
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
