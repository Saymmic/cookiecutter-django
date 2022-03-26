from rest_framework.routers import SimpleRouter

from {{ cookiecutter.project_slug }}.users.views import UserViewSet

router = SimpleRouter()

router.register("users", UserViewSet)

app_name = "users"
urlpatterns = router.urls
