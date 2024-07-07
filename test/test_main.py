import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app

client = TestClient(app)

@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_upload_file(async_client):
    with open("tests/sample_document.pdf", "rb") as file:
        response = await async_client.post("/upload", files={"file": ("sample_document.pdf", file, "application/pdf")}, data={"documentType": "pdf"})
    assert response.status_code == 200
    result = response.json()
    assert "document" in result
    assert "inference_prediction" in result

@pytest.mark.asyncio
async def test_main_page(async_client):
    response = await async_client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

# You can add more tests for OCR processing and post-processing if needed
