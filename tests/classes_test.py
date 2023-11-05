from http import HTTPStatus
from unittest.mock import Mock, patch

import pytest
import requests

from pyplayht.classes import Client


def test_client(client: Client):
    # check for available methods
    assert hasattr(client, "get_voices") and callable(client.get_voices)
    assert hasattr(client, "new_conversion_job") and callable(
        client.new_conversion_job,
    )
    assert hasattr(client, "get_coversion_job_status") and callable(
        client.get_coversion_job_status,
    )
    assert hasattr(client, "download_file") and callable(client.download_file)


@pytest.mark.parametrize(
    "method",
    [
        "GET",
        "POST",
    ],
)
def test_request(method: str, client: Client):
    response = client._request(
        method=method, path=f"https://postman-echo.com/{method.lower()}"
    )
    assert isinstance(response, requests.Response)
    assert response.status_code == HTTPStatus.OK


def test_download_file(client: Client):
    mock_request = Mock()
    mock_request.content = bytes()
    with patch("pyplayht.classes.Client._request", return_value=mock_request):
        response = client.download_file("http://127.0.0.1/test_path")
        assert isinstance(response, bytes)
