import re
from datetime import datetime, timedelta
from .models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model



class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)
    def validate_mobile(self, mobile):
        if User.objects.filter(mobile=mobile).all():
            raise serializers.ValidationError("用户已经存在")
        return mobile