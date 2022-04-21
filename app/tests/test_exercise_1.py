from flask import Flask
import json
import pytest

from .. import app

def test_print_numbers():
    client = app.test_client()
    url = '/print_numbers'
    response = client.get(url)
    assert response.status_code == 200