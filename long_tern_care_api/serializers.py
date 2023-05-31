from rest_framework import serializers
from long_tern_care_api.models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = UserManager.objects.create_user(**validated_data)
        return user
