import pytest
import page_analyzer.app as app


def test_start_page_response():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_start_page_body():
    response = app.test_client().get('/')
    assert "Анализатор страниц" in response.text




