def test_get_activities_returns_all_activities(client):
    """Test GET /activities endpoint"""
    # Arrange
    expected_activities = [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Tennis Club",
        "Art Studio",
        "Music Ensemble",
        "Debate Club",
        "Science Olympiad",
    ]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert all(activity in activities for activity in expected_activities)


def test_signup_for_activity_success(client, chess_activity, new_student_email):
    """Test successful signup for an activity"""
    # Arrange
    email = new_student_email
    activity = chess_activity

    # Act
    response = client.post(
        f"/activities/{activity}/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Signed up" in data["message"]
    assert email in data["message"]


def test_signup_duplicate_fails(client, chess_activity, registered_student_email):
    """Test that duplicate signup is rejected"""
    # Arrange
    email = registered_student_email
    activity = chess_activity

    # Act
    response = client.post(
        f"/activities/{activity}/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data["detail"].lower()


def test_signup_nonexistent_activity_fails(client, new_student_email):
    """Test that signup for non-existent activity fails"""
    # Arrange
    email = new_student_email
    activity = "Nonexistent Activity"

    # Act
    response = client.post(
        f"/activities/{activity}/signup", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"].lower()
