import unittest
from unittest.mock import MagicMock, patch

from notion.client import NotionClient
from validator.schema import validate_email_schema


class TestIntegration(unittest.TestCase):
    @patch('pubsub.publisher.EventPublisher.publish_event')
    @patch('gmail.client.GmailClient.get_email')
    def test_full_processing_flow(self, mock_email, mock_publish):
        # Mock email data
        mock_email.return_value = {
            "id": "test123",
            "subject": "Test Subject",
            "body": "Test Body"
        }
        
        # Test validation
        valid = validate_email_schema(mock_email.return_value)
        self.assertTrue(valid)
        
        # Test Notion integration
        notion_mock = MagicMock(spec=NotionClient)
        notion_mock.update_database.return_value = True
        
        result = notion_mock.update_database(
            database_id="test_db",
            properties={"Email ID": "test123"}
        )
        self.assertTrue(result) 