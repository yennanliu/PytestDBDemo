import pytest 
import unittest
from unittest.mock import Mock, patch
# UDF 
from app import call_website

class TestApp(unittest.TestCase):
    def test_call_website(self):
        with patch('app.requests') as mock_requests:
            mock_requests.get.return_value = "123"
            response = call_website()
            assert response == "123"

if __name__ == '__main__':
    pytest.main([__file__])
