import pytest
import json
import os
import page_analyzer.app as app


def test_start_page_response():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_start_page_body():
    response = app.test_client().get('/')
    path = os.getcwd()
    with open(path + '/tests/fixtures/text_check.json', 'r') as fp:
        elems = json.load(fp)
        assert all(map(lambda x: x in response.text, [elem for elem in elems]))




