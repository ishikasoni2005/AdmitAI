from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import College
from .serializers import CollegeSerializer
from accounts.models import User
from accounts.permissions import IsCollegeAdmin, IsSuperAdmin


class CollegeViewSet(viewsets.ModelViewSet):

    serializer_class = CollegeSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == User.Role.SUPER_ADMIN:
            return College.objects.all()

        if user.college:
            return College.objects.filter(
                id=user.college.id
            )

        return College.objects.none()

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            return [IsSuperAdmin()]

        if self.action in ["update", "partial_update"]:
            return [(IsSuperAdmin | IsCollegeAdmin)()]

        return [IsAuthenticated()]
