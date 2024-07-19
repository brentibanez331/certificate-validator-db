from rest_framework import serializers
# from django.contrib.auth.models import CustomUser
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'organization', 'personUserId']