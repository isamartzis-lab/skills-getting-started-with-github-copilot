def test_get_activities_returns_seeded_activity_map(client):
    # Arrange
    activities_path = "/activities"

    # Act
    response = client.get(activities_path)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "Programming Class" in payload


def test_get_activities_entries_have_expected_schema(client):
    # Arrange
    activities_path = "/activities"

    # Act
    response = client.get(activities_path)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    for activity in payload.values():
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)


def test_get_activities_chess_club_has_seeded_participants(client):
    # Arrange
    activities_path = "/activities"

    # Act
    response = client.get(activities_path)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload["Chess Club"]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]