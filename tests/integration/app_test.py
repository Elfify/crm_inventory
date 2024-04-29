def test__health(test_client):
    response = test_client.get("/health")
    response_json = response.json()

    assert response.status_code == 200
    assert response_json == {"result": "GOOD"}


def test__create_inventory__success(initialize_and_clean_db, test_client):
    # Arrange
    json={"user_id": 1, "name": "TEST_NAME", "storage_location": "TEST_STORAGE_LOCATION"}

    # Act
    response = test_client.post(
        "/inventory",
        json=json
    )
    response_json = response.json()

    # Assert
    expected_response = {
        'result': 'success',
        'data': {
            'id': 1,
            'user_id': 1,
            'name': 'TEST_NAME',
            'storage_location': 'TEST_STORAGE_LOCATION'
        }
    }
    assert response_json == expected_response
    