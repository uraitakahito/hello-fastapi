from fastapi.testclient import TestClient


class TestHandleRpc:
    def test_add(self, client: TestClient) -> None:
        response = client.post(
            "/api",
            json={
                "jsonrpc": "2.0",
                "method": "add",
                "params": {"addend1": 1, "addend2": 2},
                "id": 1,
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 3

    def test_subtract(self, client: TestClient) -> None:
        response = client.post(
            "/api",
            json={
                "jsonrpc": "2.0",
                "method": "subtract",
                "params": {"minuend": 10, "subtrahend": 3},
                "id": 2,
            },
        )
        assert response.status_code == 200
        assert response.json()["result"] == 7

    def test_multiply(self, client: TestClient) -> None:
        response = client.post(
            "/api",
            json={
                "jsonrpc": "2.0",
                "method": "multiply",
                "params": {"multiplicand": 4, "multiplier": 5},
                "id": 3,
            },
        )
        assert response.status_code == 200
        assert response.json()["result"] == 20

    def test_divide(self, client: TestClient) -> None:
        response = client.post(
            "/api",
            json={
                "jsonrpc": "2.0",
                "method": "divide",
                "params": {"dividend": 10, "divisor": 2},
                "id": 4,
            },
        )
        assert response.status_code == 200
        assert response.json()["result"] == 5

    def test_divide_by_zero(self, client: TestClient) -> None:
        response = client.post(
            "/api",
            json={
                "jsonrpc": "2.0",
                "method": "divide",
                "params": {"dividend": 10, "divisor": 0},
                "id": 5,
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert "error" in data

    def test_method_not_found(self, client: TestClient) -> None:
        response = client.post(
            "/api",
            json={
                "jsonrpc": "2.0",
                "method": "nonexistent",
                "params": {},
                "id": 6,
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert "error" in data
        assert data["error"]["code"] == -32601
