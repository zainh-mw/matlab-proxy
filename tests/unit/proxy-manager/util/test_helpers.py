# Copyright 2024-2026 The MathWorks, Inc.

from matlab_proxy_manager.utils import helpers


def test_request_session_has_correct_proxy_settings():
    """Test that requests_retry_session returns a session with proxy settings."""
    session = helpers.requests_retry_session()
    assert session.proxies is not None
    assert "no_proxy" in session.proxies


def test_check_for_server_readiness_forwards_correct_proxy_settings(mocker):
    """Test that is_server_ready forwards proxy settings to the GET request.

    Mocks the requests_retry_session to control the session object and its proxies,
    then asserts that the underlying get method is called with those proxies.
    """
    mock_response = mocker.MagicMock()
    mock_proxies = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.text = "MWI_MATLAB_PROXY_IDENTIFIER"
    mock_req_retry_session = mocker.patch(
        "matlab_proxy_manager.utils.helpers.requests_retry_session"
    )
    mock_req_retry_session.return_value.get.return_value = mock_response
    mock_req_retry_session.return_value.proxies = mock_proxies

    response = helpers.is_server_ready("http://localhost:8888")

    mock_req_retry_session.return_value.get.assert_called_once_with(
        url="http://localhost:8888",
        proxies=mock_proxies,
        verify=False,
    )
    assert response is True
