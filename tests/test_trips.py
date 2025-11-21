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

def test_create_trip_with_rate(client):
    response = client.post(
        "/trips/upload-rate-confirmation",
        data={"type": "RATE_CONFIRMATION"},
        files={"file": ("rate_confirmation.pdf", b"content", "application/pdf")}
    )
    assert response.status_code == 200
    data = response.json()

    # Verify Document Response
    assert "trip_id" in data
    assert data["type"] == "RATE_CONFIRMATION"
    assert data["file_url"] == "local_files/rate_confirmation.pdf"

    # Verify Trip Creation
    trip_id = data["trip_id"]
    trip_response = client.get(f"/trips/{trip_id}")
    assert trip_response.status_code == 200
    trip_data = trip_response.json()

    # Check if OCR data was applied
    assert trip_data["pickup_city"] == "New York"
    assert trip_data["dropoff_city"] == "Los Angeles"
    assert trip_data["broker_id"] == "CHROBINSON"
    assert trip_data["rate"] == 100

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
