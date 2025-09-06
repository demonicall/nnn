from rest_framework import serializers
from users.models import Users
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = Users
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        # return Users.objects.create(**validated_data)
        user = Users.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user

    # def validate_email(self, value):
    #     if Users.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("Email already taken")
    #     return value

    def validate_password(self, value):
        try:
            validate_password(value)  # runs Django's configured validators
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value