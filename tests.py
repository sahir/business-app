import pytest
from fastapi.testclient import TestClient
from app import app
import time

client = TestClient(app)
business_data = {}

@pytest.mark.order(3)
def test_create_business():
    global business_data
    business_data = {
        "name": f"DwellFi-{int(time.time())}",
        "legal_name":"DwellFi",
        "address": "Palo Alto, California, United States",
        "owner_info": "Test Owner",
        "employee_size": 10,
        "phone_number": f"123-{int(time.time())}",
        "contact_email": f"test-{int(time.time())}@dwell.fi",
        "founded_date": "2023-07-31",
        "founders":"kumar",
        "last_funding_type": "Convertible Note"
    }
    response = client.post("/business/", json=business_data)
    assert response.status_code == 200
    business_data = response.json()

@pytest.mark.order(2)
def test_read_business():
    global business_data
    if business_data:
        response = client.get(f"/business/{business_data.get('id')}")
        assert response.status_code == 200

@pytest.mark.order(1)
def test_update_business():
    global business_data
    updated_data = {
        "name": f"Updated Business{int(time.time())}",
        "address": "Updated Address",
        "owner_info": "Updated Owner",
        "employee_size": 20,
        "contact_email": f"test-{int(time.time())}@example.com",
        "phone_number": f"123-{int(time.time())}",
    }
    response = client.put(f"/business/{business_data.get('id')}", json=updated_data)
    
    assert response.status_code == 200


def test_read_nonexistent_business():
    response = client.get("/business/10")
    assert response.status_code == 404

def test_update_nonexistent_business():
    updated_data = {
        "name": f"Updated Business-{int(time.time())}",
        "address": "Updated Address",
        "owner_info": "Updated Owner",
        "employee_size": 20,
    }
    response = client.put("/business/100", json=updated_data)
    assert response.status_code == 404


def test_delete_business():
    global business_data
    response = client.delete(f"/business/{business_data.get('id')}")
    assert response.status_code == 200
    response = client.get(f"/business/{business_data.get('id')}")
    assert response.status_code == 404


def test_delete_nonexistent_business():
    response = client.delete("/business/1000")
    assert response.status_code == 404


def test_search_business():
    response = client.get("/business/")
    assert response.status_code == 200
    assert len(response.json()) > 1
