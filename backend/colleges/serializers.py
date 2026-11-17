from rest_framework import serializers
from .models import College


class CollegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "address",
            "city",
            "state",
            "website",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]