from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        COLLEGE_ADMIN = "COLLEGE_ADMIN", "College Admin"
        COUNSELLOR = "COUNSELLOR", "Counsellor"
        STUDENT = "STUDENT", "Student"

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    college = models.ForeignKey(
        "colleges.College",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users",
    )

    def __str__(self):
        return self.email