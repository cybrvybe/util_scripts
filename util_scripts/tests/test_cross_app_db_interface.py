import unittest
from unittest.mock import patch, MagicMock
from nexus_db.nexus_db.core.api.db_direct_access_point import DbDirectAccessPoint
from nexus_db.nexus_db.core.api.cross_app_db_interface import CrossAppDbInterface

class TestCrossAppDbInterface(unittest.TestCase):
    @patch.object(DbDirectAccessPoint, 'create_schema')
    def test_create_schema(self, mock_create_schema):
        cross_app_db_interface = CrossAppDbInterface(schema_name="test_schema")
        cross_app_db_interface.create_schema()

        mock_create_schema.assert_called_with("test_schema")

    # Similar tests can be written for the other methods.

if __name__ == "__main__":
    unittest.main()
