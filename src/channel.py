import os
import json
from googleapiclient.discovery import build
# os.environ['YT_API_KEY'] = 'AIzaSyAqj90FsgBsLUtc0bQYebwrFW4o8Hi-qSk'
api_key = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_info = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.channel_name = self.channel_info.get
        self.channel_desc = None
        self.channel_link = None
        self.channel_subscribers_count = None
        self.channel_videos_count = None
        self.views_count = None


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        response = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(response, indent=2, ensure_ascii=False))
