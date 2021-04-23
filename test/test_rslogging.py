# ********************************
# |docname| - test the logging API
# ********************************

from fastapi.testclient import TestClient
from bookserver.schemas import LogItemIncoming
from bookserver.main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200


def test_add_log():
    item = LogItemIncoming(
        event="page",
        act="view",
        div_id="/runestone/fopp/index.html",
        sid="testuser",
        course_name="fopp",
    )
    response = client.post(
        "/logger/bookevent",
        headers={"Content-type": "application/json; charset=utf-8"},
        json=item.dict(),
    )
    assert response.status_code == 200
    assert response.json()["status"] == "OK"
