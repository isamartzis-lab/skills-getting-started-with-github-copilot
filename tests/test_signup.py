def test_signup_adds_new_student_to_existing_activity(client, known_activity_name, sample_email):
    # Arrange
    signup_path = f"/activities/{known_activity_name}/signup"
    params = {"email": sample_email}

    # Act
    response = client.post(signup_path, params=params)
    activities_response = client.get("/activities")
    participants = activities_response.json()[known_activity_name]["participants"]

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {sample_email} for {known_activity_name}"
    assert sample_email in participants


def test_signup_rejects_student_already_signed_up(client, known_activity_name):
    # Arrange
    existing_email = "michael@mergington.edu"
    signup_path = f"/activities/{known_activity_name}/signup"
    params = {"email": existing_email}

    # Act
    response = client.post(signup_path, params=params)

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_signup_rejects_unknown_activity(client, unknown_activity_name, sample_email):
    # Arrange
    signup_path = f"/activities/{unknown_activity_name}/signup"
    params = {"email": sample_email}

    # Act
    response = client.post(signup_path, params=params)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"