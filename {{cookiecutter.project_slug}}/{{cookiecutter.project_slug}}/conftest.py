import pytest
from rest_framework.test import APIClient

from {{ cookiecutter.project_slug }}.users.models import User
from {{ cookiecutter.project_slug }}.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def test_user() -> User:

    return UserFactory.create(
        username="APITestUser",
        email="api_test_user@gmail.com",
        name="API Test User",
    )


@pytest.fixture
def api_client(test_user) -> APIClient:
    api_client = APIClient()
    api_client.force_authenticate(user=test_user)

    return api_client
