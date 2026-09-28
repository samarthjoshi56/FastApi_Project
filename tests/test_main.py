from app.main import app


def test_root(client) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "FastAPI is running",
        "version": app.version,
    }


def test_health(client) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_user_search_by_name(client) -> None:
    client.post(
        "/users",
        json={"name": "Alice Smith", "email": "alice@example.com"},
    )
    client.post(
        "/users",
        json={"name": "Bob Jones", "email": "bob@example.com"},
    )

    response = client.get("/users", params={"name": "alice"})

    assert response.status_code == 200
    assert response.json()[0]["name"] == "Alice Smith"


def test_user_search_returns_empty_for_no_match(client) -> None:
    response = client.get("/users", params={"name": "does-not-exist"})

    assert response.status_code == 200
    assert response.json() == []
