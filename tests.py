import pytest
from flask import Flask

# import your Flask app from the app file
from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert b'Welcome to the calculator!' in response.data

def test_add(client):
    response = client.post('/add', data=dict(num1=5, num2=10))
    assert b'The sum of 5 and 10 is 15.0' in response.data


def test_subtract(client):
    response = client.post('/subtract', data=dict(num1=5, num2=10))
    assert b'The difference between 5 and 10 is -5.0' in response.data


def test_multiply(client):
    response = client.post('/multiply', data=dict(num1=5, num2=10))
    assert b'The product of 5 and 10 is 50.0' in response.data


def test_divide(client):
    response = client.post('/divide', data=dict(num1=5, num2=10))
    assert b'The quotient of 5 and 10 is 0.5' in response.data


def test_divide_by_zero(client):
    response = client.post('/divide', data=dict(num1=5, num2=0))
    assert b'Error: cannot divide by zero' in response.data
