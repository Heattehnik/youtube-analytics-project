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

    def show(self):
        return self.video_response

if __name__ == '__main__':
    video = Video('9lO06Zxhu88')
    print(video.show())