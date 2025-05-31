from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())], #전체를 불러오는 것 외의 비교 방법 없음        
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password" : "Password fields didn't match."}
            )
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        #password를 다른 처리를 할 수 있기에 따로 빼내서 설정
        user.set_password(validated_data['password'])
        user.save()

        tocken = Token.objects.create(user=user)
        return user
    
class LoginSerializer(serializers.Serializer): #로그인 기능이 모델과 직접적인 매핑이 필요하지 않기 때문에 ModelSerializer를 안 씀
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(username = data['username'], password = data['password'])
        
        if user: #user에 뭐가 들어있으면 인증 성공한것
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with previded credentials."}
        )
    
class ProfileSerializer(serializers.ModelSerializer): #model에서 상속 받는거니  ModelSerializer를 씀
    class Meta:
        model = Profile
        fields = ("nickname", "position", "subjects")