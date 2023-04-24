from dotenv import load_dotenv
from googleapiclient.discovery import build
import os
import datetime
import isodate

load_dotenv()


class PlayList:
    """
    Класс для работы с плейлистами youtube
    """
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(id=playlist_id,
                                                      part='contentDetails, snippet',
                                                      maxResults=50,
                                                      ).execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/playlist?list=" + playlist_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()
        self.videos_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(self.videos_ids)).execute()

    @property
    def total_duration(self):
        """
        Определение полной продолжительности видео в плейлисте
        """
        full_duration = datetime.timedelta(seconds=0)
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            full_duration += duration
        return full_duration

    def show_best_video(self):
        """Поиск самого залайконого видео)))"""
        most_liked = 0
        url = None
        for video in self.video_response['items']:
            likes_count = int(video['statistics']['likeCount'])
            if most_liked < likes_count:
                most_liked = likes_count
                url = "https://youtu.be/" + video['id']

        return url
