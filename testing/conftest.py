import pytest
from main import app
from UserModels import db


@pytest.fixture()
def client():
    return app.test_client()
