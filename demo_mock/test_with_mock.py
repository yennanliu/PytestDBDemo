import pytest 
import unittest
from unittest.mock import Mock, patch
from requests.exceptions import Timeout
# UDF 
from app import call_website, call_website_if_status

class TestApp(unittest.TestCase):
    def test_call_website(self):
        with patch('app.requests') as mock_requests:
            mock_requests.get.return_value = "123"
            response = call_website()
            assert response == "123"

    def test_call_website_if_status(self):
        with patch('app.requests') as mock_requests:
            mock_requests.get.status_code = 200
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                response = call_website_if_status()
                ### TO FIX : mock_requests.get_call_count assertion 
                #assert mock_requests.get_call_count == 2
                assert response == None

if __name__ == '__main__':
    pytest.main([__file__])
