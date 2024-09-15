from datetime import datetime

import pytest
from flask import session

from app.main import app, fibonacci


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def text_index_initial(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Fibonacci number: 0" in response.data
    assert session["count"] == 0
    
    response = client.get("/")
    assert response.status_code == 200
    assert b"Fibonacci number: 1" in response.data
    assert session["count"] == 1
    
    response = client.get("/")
    assert b"Fibonacci number: 1" in response.data
    assert session["count"] == 2


def test_inject_globals(client):
    current_date = datetime.now().strftime("%d/%m/%Y").encode("utf-8")
    response = client.get("/")
    assert current_date in response.data


@pytest.mark.parametrize(
    "count, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144),
        (13, 233),
        (14, 377),
        (15, 610),
        (16, 987),
        (17, 1597),
        (18, 2584),
        (19, 4181),
    ],
)
def test_fibonacci(count, expected):
    assert fibonacci(count) == expected
