from django.db import models
from core.models import TimeStampedModel


class Course(TimeStampedModel):

    college = models.ForeignKey(
        "colleges.College",
        on_delete=models.CASCADE,
        related_name="courses",
    )

    name = models.CharField(max_length=255)

    code = models.CharField(
        max_length=50,
        blank=True,
    )

    degree = models.CharField(
        max_length=100,
        blank=True,
    )

    department = models.CharField(
        max_length=150,
        blank=True,
    )

    duration_years = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    annual_fee = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    total_seats = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["college", "name"],
                name="unique_course_per_college",
            )
        ]

        indexes = [
            models.Index(fields=["college", "is_active"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.college.name}"


class EligibilityRule(TimeStampedModel):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="eligibility_rules",
    )

    minimum_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )

    required_subjects = models.JSONField(
        default=list,
        blank=True,
    )

    entrance_required = models.BooleanField(
        default=False,
    )

    entrance_exam = models.CharField(
        max_length=100,
        blank=True,
    )

    minimum_entrance_score = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    additional_requirements = models.JSONField(
        default=dict,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"Eligibility Rule - {self.course.name}"