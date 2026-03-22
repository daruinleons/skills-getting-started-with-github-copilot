def test_unregister_success(client, chess_activity, registered_student_email):
    """Test successful unregistration from activity"""
    # Arrange
    email = registered_student_email
    activity = chess_activity

    # Act
    response = client.delete(
        f"/activities/{activity}/unregister", params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Unregistered" in data["message"]


def test_unregister_not_registered_fails(client, chess_activity, new_student_email):
    """Test that unregistering non-registered student fails"""
    # Arrange
    email = new_student_email
    activity = chess_activity

    # Act
    response = client.delete(
        f"/activities/{activity}/unregister", params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "not registered" in data["detail"].lower()


def test_unregister_nonexistent_activity_fails(client, registered_student_email):
    """Test that unregistering from non-existent activity fails"""
    # Arrange
    email = registered_student_email
    activity = "Nonexistent Activity"

    # Act
    response = client.delete(
        f"/activities/{activity}/unregister", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"].lower()
