import pytest
from unittest.mock import patch

def test_upload_document(client):
    # 1. Create a trip first
    trip_response = client.post(
        "/trips/",
        json={"pickup_city": "Boston", "dropoff_city": "Austin"}
    )
    trip_id = trip_response.json()["id"]

    # 2. Mock the upload_service so we don't actually save files
    with patch("app.routers.documents.upload_document") as mock_upload:
        mock_upload.return_value = "local_files/test_doc.pdf"
        
        # 3. Upload a file
        response = client.post(
            f"/trips/{trip_id}/documents",
            data={"type": "BOL"},
            files={"file": ("test_doc.pdf", b"fake content", "application/pdf")}
        )

    # 4. Verify response
    assert response.status_code == 200
    data = response.json()
    assert data["trip_id"] == trip_id
    assert data["type"] == "BOL"
    assert data["file_url"] == "local_files/test_doc.pdf"

def test_list_documents(client):
    # 1. Create trip and document
    trip_response = client.post("/trips/", json={"pickup_city": "A", "dropoff_city": "B"})
    trip_id = trip_response.json()["id"]
    
    with patch("app.routers.documents.upload_document") as mock_upload:
        mock_upload.return_value = "local_files/doc.pdf"
        client.post(
            f"/trips/{trip_id}/documents",
            data={"type": "POD"},
            files={"file": ("doc.pdf", b"content", "application/pdf")}
        )

    # 2. List documents
    response = client.get(f"/trips/{trip_id}/documents")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["type"] == "POD"
