from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from drf_tutorial.users.api.views import UserViewSet
from drf_tutorial.quickstart.views import UserQViewSet
from drf_tutorial.quickstart.views import GroupQViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("another_users", UserQViewSet)
router.register("groups", GroupQViewSet)


app_name = "api"
urlpatterns = router.urls
