import os
import json
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()


class Channel:
    """Класс для ютуб-канала"""

    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    @classmethod
    def get_service(cls):
        """ Возвращает экземпляр класса Channel"""

        return cls.youtube

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.desc = self.channel_info['items'][0]['snippet']['description']
        self.url = self.channel_info['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscribers_count = int(self.channel_info['items'][0]['statistics']['subscriberCount'])
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.views_count = self.channel_info['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f"'{self.title} ({self.url})'"

    def __add__(self, other):
        return self.subscribers_count + other.subscribers_count

    def __sub__(self, other):
        return self.subscribers_count - other.subscribers_count

    def __gt__(self, other):
        return self.subscribers_count > other.subscribers_count

    def __ge__(self, other):
        return self.subscribers_count >= other.subscribers_count

    def __lt__(self, other):
        return self.subscribers_count < other.subscribers_count

    def __le__(self, other):
        return self.subscribers_count <= other.subscribers_count

    def __eq__(self, other):
        return self.subscribers_count == other.subscribers_count

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel_info, indent=2, ensure_ascii=False))

    def to_json(self, filename):
        """
        Метод сохраняет данные о канале в файл json
        """
        with open(filename, 'a+', encoding='utf-8') as f:
            data = {
                'channel_id': self.__channel_id,
                'title': self.title,
                'description': self.desc,
                'url': self.url,
                'subscribers_count': self.subscribers_count,
                'video_count': self.video_count,
                'views_count': self.views_count
            }
            json.dump(data, f, ensure_ascii=False)
