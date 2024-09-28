from unittest.mock import patch


@patch('src.external_api.requests.request')
def test_q(mock_api):
    mock_api.return_value = {'result': 12345.671}
    pass
