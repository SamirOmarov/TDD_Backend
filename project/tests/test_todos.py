import json
import pytest


def test_create_todo(test_app):
    response = test_app.post("/todo/", data=json.dumps({"title": "TDD Test"}))
    assert response.status_code == 201
    assert response.json()["title"] == "TDD Test"


def test_create_todo_invalid_json(test_app):
    response = test_app.post("/todo/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "title"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_get_all_todos(test_app):
    response = test_app.post("/todo/", data=json.dumps({"title": "TDD Test"}))
    todo_id = response.json()["id"]

    response = test_app.get("/todo/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == todo_id, response_list))) == 1
