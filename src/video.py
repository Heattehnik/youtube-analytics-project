from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()


class Video:
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id
        self.video_response = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                          id=self.video_id).execute()
        self.video_title = self.video_response['items'][0]['snippet']['title']
        self.video_url = self.video_response['items'][0]['snippet']['thumbnails']['default']['url']
        self.views_count = self.video_response['items'][0]['statistics']['viewCount']
        self.likes_count = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.video_title}'


class PLVideo(Video):

    def __init__(self, video_id, pl_id):
        self.pl_id = pl_id
        super().__init__(video_id)




