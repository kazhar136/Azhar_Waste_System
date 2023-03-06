from rest_framework import serializers
from .models import Waste
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'password']

class WasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waste
        fields = "__all__"
    

