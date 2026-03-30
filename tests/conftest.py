"""Shared pytest fixtures for FastAPI backend tests."""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


BASELINE_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore in-memory activity state before each test for isolation."""
    app_module.activities.clear()
    app_module.activities.update(deepcopy(BASELINE_ACTIVITIES))
    yield


@pytest.fixture
def client():
    """Provide a FastAPI TestClient for endpoint tests."""
    with TestClient(app_module.app) as test_client:
        yield test_client


@pytest.fixture
def known_activity_name():
    """Activity name known to exist in seeded data."""
    return "Chess Club"


@pytest.fixture
def unknown_activity_name():
    """Activity name that does not exist in seeded data."""
    return "Astronomy Club"


@pytest.fixture
def sample_email():
    """Email not present in the seeded participant lists."""
    return "newstudent@mergington.edu"