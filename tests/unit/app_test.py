def test__health(test_client):
    response = test_client.get("/health")
    response_json = response.json()

    assert response.status_code == 200
    assert response_json == {"result": "GOOD"}
