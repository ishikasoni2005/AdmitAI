from django.contrib import admin
from .models import Course, EligibilityRule


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "college",
        "degree",
        "department",
        "annual_fee",
        "total_seats",
        "is_active",
    )

    list_filter = (
        "college",
        "degree",
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "department",
    )


@admin.register(EligibilityRule)
class EligibilityRuleAdmin(admin.ModelAdmin):

    list_display = (
        "course",
        "minimum_percentage",
        "entrance_required",
        "entrance_exam",
        "is_active",
    )

    list_filter = (
        "entrance_required",
        "is_active",
    )