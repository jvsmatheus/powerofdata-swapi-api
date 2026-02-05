import os

API_KEY = os.getenv("API_KEY")

def test_list_people_success(client, monkeypatch):
    def mock_get(self, resource):
        return {
            "results": [
                {"name": "Luke Skywalker", "gender": "male"}
            ]
        }

    monkeypatch.setattr(
        "app.clients.swapi_client.SwapiClient.get",
        mock_get
    )

    response = client.get(
        "/api/people",
        headers={"x-api-key": API_KEY}
    )

    assert response.status_code == 200
    body = response.get_json()

    assert body["success"] is True
    assert body["count"] == 1
    assert body["data"][0]["name"] == "Luke Skywalker"
    
def test_filter_people_by_gender(client, monkeypatch):
    def mock_get(self, resource):
        return {
            "results": [
                {"name": "Luke", "gender": "male"},
                {"name": "Leia", "gender": "female"}
            ]
        }

    monkeypatch.setattr(
        "app.clients.swapi_client.SwapiClient.get",
        mock_get
    )

    response = client.get(
        "/api/people?gender=male",
        headers={"x-api-key": API_KEY}
    )

    body = response.get_json()

    assert body["count"] == 1
    assert body["data"][0]["name"] == "Luke"
    
def test_sort_people_by_name(client, monkeypatch):
    def mock_get(self, resource):
        return {
            "results": [
                {"name": "Leia"},
                {"name": "Luke"}
            ]
        }

    monkeypatch.setattr(
        "app.clients.swapi_client.SwapiClient.get",
        mock_get
    )

    response = client.get(
        "/api/people?sort=name",
        headers={"x-api-key": API_KEY}
    )

    body = response.get_json()

    assert body["data"][0]["name"] == "Leia"