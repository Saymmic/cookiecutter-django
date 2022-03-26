from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("", include("{{ cookiecutter.project_slug }}.users.urls")),
]

