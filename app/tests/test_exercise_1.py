from flask import Flask
import json
import pytest

from .. import app

def test_status_code_200():
    client = app.test_client()
    url = '/print_numbers'
    response = client.get(url)
    assert response.status_code == 200
    
def test_numbers_in_response_dict():
    client = app.test_client()
    url = '/print_numbers'
    response = client.get(url)
    resp_dict = json.loads(response.text)
    assert "numbers" in resp_dict
    
def test_response_type_is_a_list():
    client = app.test_client()
    url = '/print_numbers'
    response = client.get(url)
    resp_dict = json.loads(response.text)
    assert isinstance(resp_dict["numbers"], list)
    
def test_numbers_list_not_empty():
    client = app.test_client()
    url = '/print_numbers'
    response = client.get(url)
    resp_dict = json.loads(response.text)
    assert len(resp_dict["numbers"]) > 0
    
def test_numbers_length_eq_100():
    client = app.test_client()
    url = '/print_numbers'
    response = client.get(url)
    resp_dict = json.loads(response.text)
    assert len(resp_dict["numbers"]) == 100
    
def test_if_three_is_printed():
    client = app.test_client()
    url = '/print_numbers'
    response = client.get(url)
    resp_dict = json.loads(response.text)
    assert resp_dict["numbers"][2] == "Three"
    
def test_if_five_is_printed():
    client = app.test_client()
    url = '/print_numbers'
    response = client.get(url)
    resp_dict = json.loads(response.text)
    assert resp_dict["numbers"][4] == "Five"
    
def test_if_threefive_is_printed():
    client = app.test_client()
    url = '/print_numbers'
    response = client.get(url)
    resp_dict = json.loads(response.text)
    assert resp_dict["numbers"][14] == "ThreeFive"