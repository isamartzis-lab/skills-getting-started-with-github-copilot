def test_unregister_removes_existing_student_from_activity(client, known_activity_name):
    # Arrange
    existing_email = "michael@mergington.edu"
    unregister_path = f"/activities/{known_activity_name}/unregister"
    params = {"email": existing_email}

    # Act
    response = client.delete(unregister_path, params=params)
    activities_response = client.get("/activities")
    participants = activities_response.json()[known_activity_name]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {existing_email} from {known_activity_name}"
    assert existing_email not in participants


def test_unregister_rejects_unknown_activity(client, unknown_activity_name, sample_email):
    # Arrange
    unregister_path = f"/activities/{unknown_activity_name}/unregister"
    params = {"email": sample_email}

    # Act
    response = client.delete(unregister_path, params=params)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_rejects_student_not_signed_up(client, known_activity_name, sample_email):
    # Arrange
    unregister_path = f"/activities/{known_activity_name}/unregister"
    params = {"email": sample_email}

    # Act
    response = client.delete(unregister_path, params=params)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"