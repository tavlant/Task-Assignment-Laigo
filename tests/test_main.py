import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from main import app  

from fastapi.testclient import TestClient

client = TestClient(app)

def test_upload_file():
    with open("tests/test_invoice.pdf", "rb") as file:
        response = client.post("/upload", files={"file": file})
        assert response.status_code == 200
        assert "document" in response.json()
        assert "inference_prediction" in response.json()
