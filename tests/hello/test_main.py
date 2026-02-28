from fastapi.testclient import TestClient


class TestReadRoot:
    def test_returns_hello_world(self, client: TestClient) -> None:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
