def test_create_trip(client):
    response = client.post(
        "/trips/",
        json={"pickup_city": "New York", "dropoff_city": "Los Angeles", "driver_id": 1, "broker_id": "B123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["pickup_city"] == "New York"
    assert data["dropoff_city"] == "Los Angeles"
    assert "id" in data

def test_list_trips(client):
    # Create a trip first
    client.post(
        "/trips/",
        json={"pickup_city": "Chicago", "dropoff_city": "Miami"}
    )
    
    response = client.get("/trips/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["pickup_city"] == "Chicago"
