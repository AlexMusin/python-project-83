import pytest
import page_analyzer.app as app


def test_start_page():
    response = app.test_client().get('/')
    assert response.status_code == 200




