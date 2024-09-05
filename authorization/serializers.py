from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SignInSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(SignInSerializer, cls).get_token(user)

        token['username'] = user.username
        return token

    # def validate(self, attrs):
    #     data = super().validate(attrs)
    #     refresh_token = data["refresh"]
    #     access_token = data["access"]
    #
    #     response_data = {
    #         'status': 1,
    #         'data': {
    #             'refresh': str(refresh_token),
    #             'access': str(access_token)
    #         }
    #     }
    #
    #     return response_data


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            "status": 1,
            "data": representation
        }
