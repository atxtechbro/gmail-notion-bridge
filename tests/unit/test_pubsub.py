import json
from unittest.mock import Mock, patch

from pubsub.publisher import EventPublisher


def test_publish_event_success():
    mock_client = Mock()
    with patch('pubsub_v1.PublisherClient', return_value=mock_client):
        publisher = EventPublisher("test-project", "test-topic")
        test_data = {"email_id": "test123", "received_at": "2024-01-01T00:00:00Z"}
        
        result = publisher.publish_event(test_data)
        
        mock_client.topic_path.assert_called_once_with("test-project", "test-topic")
        mock_client.publish.assert_called_once_with(
            publisher.topic_path,
            data=json.dumps(test_data).encode("utf-8")
        )
        assert result == mock_client.publish.return_value.result.return_value
