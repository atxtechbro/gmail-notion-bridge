from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


class GmailClient:
    def __init__(self, token_path: str, scopes: list[str]):
        self.creds = Credentials.from_authorized_user_file(token_path, scopes)
        self.service = build('gmail', 'v1', credentials=self.creds)
    
    def watch_labels(self, label_ids: list[str], pubsub_topic: str):
        return self.service.users().watch(
            userId='me',
            body={
                'labelIds': label_ids,
                'topicName': pubsub_topic
            }
        ).execute() 