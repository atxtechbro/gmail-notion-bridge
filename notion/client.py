from notion_client import Client


class NotionBaseClient:
    def __init__(self, api_token: str):
        self.client = Client(auth=api_token)
    
    def create_page(self, database_id: str, properties: dict):
        return self.client.pages.create(
            parent={"database_id": database_id},
            properties=properties
        ) 