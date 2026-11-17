from django.contrib import admin
from .models import College


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "city",
        "state",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "city",
    )

    list_filter = (
        "is_active",
        "state",
    )