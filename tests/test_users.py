from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_and_get_user() -> None:
    create_response = client.post(
        "/users",
        json={"name": "Ada Lovelace", "email": "ada@example.com"},
    )

    assert create_response.status_code == 201
    user_id = create_response.json()["id"]

    response = client.get(f"/users/{user_id}")

    assert response.status_code == 200
    assert response.json() == {
        "id": user_id,
        "name": "Ada Lovelace",
        "email": "ada@example.com",
    }


def test_get_missing_user() -> None:
    response = client.get("/users/99999")

    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
