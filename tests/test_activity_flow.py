def test_student_can_signup_then_unregister_in_sequence(client, known_activity_name, sample_email):
    # Arrange
    signup_path = f"/activities/{known_activity_name}/signup"
    unregister_path = f"/activities/{known_activity_name}/unregister"
    params = {"email": sample_email}

    # Act
    signup_response = client.post(signup_path, params=params)
    unregister_response = client.delete(unregister_path, params=params)
    activities_response = client.get("/activities")
    participants = activities_response.json()[known_activity_name]["participants"]

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200
    assert sample_email not in participants