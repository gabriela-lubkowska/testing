import pytest
from unittest.mock import patch
from functions.network import get_ip_address

def test_check_proxy(monkeypatch):
    proxy = "http://127.0.0.1:8080"
    monkeypatch.setenv("http_proxy", proxy)

    from functions.network import check_proxy
    result = check_proxy()
    assert proxy in result
    assert "Proxy enabled:" in result

@patch('socket.gethostname')
@patch('socket.gethostbyname')
def test_get_ip_address(mock_gethostbyname, mock_gethostname):
    mock_gethostname.return_value = 'test_host'
    mock_gethostbyname.return_value = '127.0.0.1'

    result = get_ip_address()
    assert result == 'Twoje IP: 127.0.0.1'