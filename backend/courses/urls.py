from rest_framework.routers import DefaultRouter

from .views import (
    CourseViewSet,
    EligibilityRuleViewSet,
)


router = DefaultRouter()

router.register(
    "courses",
    CourseViewSet,
    basename="course",
)

router.register(
    "eligibility-rules",
    EligibilityRuleViewSet,
    basename="eligibility-rule",
)


urlpatterns = router.urls