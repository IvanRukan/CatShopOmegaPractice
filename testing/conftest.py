import pytest
from main import app


@pytest.fixture()
def client():
    return app.test_client()
