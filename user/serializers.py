from rest_framework import serializers

from .models import User


class UserSerializerAdmin(serializers.ModelSerializer):
    is_staff = serializers.BooleanField()
    storage_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "full_name", "email", "is_staff", "storage_id"]

    def get_storage_id(self, obj):
        """
        Returns data for storage_id field
        """
        return obj.storage.pk


class UserSerializer(serializers.ModelSerializer):
    storage_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "full_name", "email", "storage_id"]

    def get_storage_id(self, obj):
        """
        Returns data for storage_id field
        """
        return obj.storage.pk