import unittest
from unittest.mock import patch, MagicMock
from nexus_db.core.api.db_direct_access_point import DbDirectAccessPoint

class TestDbDirectAccessPoint(unittest.TestCase):
    @patch('requests.post')
    def test_create_db(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response

        db_direct_access_point = DbDirectAccessPoint()
        response = db_direct_access_point.create_db("test_db")

        self.assertEqual(response, {"status": "success"})

    # Similar tests can be written for the other methods.

if __name__ == "__main__":
    unittest.main()
