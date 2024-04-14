from rest_framework import serializers
from accounts.models import CustomUser as User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and confirm password doesn't match.")
        return attrs
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['message'] = 'Account registration successfull. Please confirm your email to login.'
        return representation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username','email', 'first_name', 'last_name']

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username','email', 'first_name', 'last_name', 'is_staff']

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)