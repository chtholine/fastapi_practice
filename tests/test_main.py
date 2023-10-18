from app.schemas.schemas import SignUpRequest


def test_healthcheck(test_client):
    response = test_client.get("/")
    assert response.status_code == 200


def test_user_create_schema_validation():
    valid_data = {
        "user_email": "user@example.com",
        "user_firstname": "John",
        "user_lastname": "Doe",
        "user_status": "active",
        "user_city": "New York",
        "user_phone": "123-456-7890",
        "user_links": "https://example.com",
        "user_avatar": "avatar.jpg",
        "hashed_password": "hashed_password",
        "is_superuser": False,
    }

    user_signup = SignUpRequest(**valid_data)
    assert user_signup.model_dump() == valid_data

    invalid_data = {
        "user_email": "user@example.com",
        # Missing "user_firstname"
        "user_lastname": "Doe",
    }

    try:
        SignUpRequest(**invalid_data)
    except ValueError:
        pass
