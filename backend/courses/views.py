from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import Course, EligibilityRule
from .serializers import (
    CourseSerializer,
    EligibilityRuleSerializer,
)
from accounts.permissions import IsCollegeStaff


class CourseViewSet(viewsets.ModelViewSet):

    serializer_class = CourseSerializer

    permission_classes = [
        IsCollegeStaff,
    ]

    def get_queryset(self):

        return Course.objects.filter(
            college=self.request.user.college
        ).select_related("college")

    def perform_create(self, serializer):

        serializer.save(
            college=self.request.user.college
        )


class EligibilityRuleViewSet(viewsets.ModelViewSet):

    serializer_class = EligibilityRuleSerializer

    permission_classes = [
        IsCollegeStaff,
    ]

    def get_queryset(self):
        return EligibilityRule.objects.filter(
            course__college=self.request.user.college
        ).select_related("course")

    def perform_create(self, serializer):
        course = serializer.validated_data.get("course")
        if course.college_id != self.request.user.college_id:
            raise ValidationError({"course": "Course must belong to your college."})
        serializer.save()

    def perform_update(self, serializer):
        course = serializer.validated_data.get("course", serializer.instance.course)
        if course.college_id != self.request.user.college_id:
            raise ValidationError({"course": "Course must belong to your college."})
        serializer.save()
