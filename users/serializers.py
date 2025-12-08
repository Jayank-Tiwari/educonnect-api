from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer CustomerUser to/from JSON.
    """
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'is_professor', 'is_student', 'first_name', 'last_name'
        ]
        read_only_fields = ['id']