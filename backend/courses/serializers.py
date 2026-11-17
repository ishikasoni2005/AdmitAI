from rest_framework import serializers
from .models import Course, EligibilityRule


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
            "id",
            "college",
            "name",
            "code",
            "degree",
            "department",
            "duration_years",
            "description",
            "annual_fee",
            "total_seats",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "college",
            "created_at",
            "updated_at",
        ]


class EligibilityRuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EligibilityRule
        fields = [
            "id",
            "course",
            "minimum_percentage",
            "required_subjects",
            "entrance_required",
            "entrance_exam",
            "minimum_entrance_score",
            "additional_requirements",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
