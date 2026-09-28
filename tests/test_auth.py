def test_register_login_and_me(client) -> None:
    register_response = client.post(
        "/auth/register",
        json={
            "name": "Ada Lovelace",
            "email": "ada-auth@example.com",
            "password": "correct-horse-battery",
        },
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/auth/login",
        json={
            "email": "ada-auth@example.com",
            "password": "correct-horse-battery",
        },
    )

    assert login_response.status_code == 200
    token = login_response.json()["access_token"]

    me_response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert me_response.status_code == 200
    assert me_response.json()["email"] == "ada-auth@example.com"


def test_login_rejects_wrong_password(client) -> None:
    client.post(
        "/auth/register",
        json={
            "name": "Grace Hopper",
            "email": "grace-auth@example.com",
            "password": "correct-password",
        },
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "grace-auth@example.com",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401


def test_me_requires_authentication(client) -> None:
    response = client.get("/auth/me")
    assert response.status_code == 401
