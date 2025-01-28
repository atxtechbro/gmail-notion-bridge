import json

from google.cloud import pubsub_v1


class EventPublisher:
    def __init__(self, project_id: str, topic_id: str):
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(project_id, topic_id)
    
    def publish_event(self, email_data: dict) -> str:
        data = json.dumps(email_data).encode("utf-8")
        return self.publisher.publish(self.topic_path, data).result() 