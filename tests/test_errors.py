def test_unauthorized_request(client):
    response = client.get("/api/people")

    assert response.status_code == 401
    body = response.get_json()
    assert body["success"] is False