from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import isodate
import datetime

load_dotenv()


class PlayList:
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_info = self.youtube.playlists().list(id=playlist_id,
                                                      part='contentDetails,'
                                                           'snippet',
                                                      maxResults=50,
                                                      ).execute()
        print(self.playlist_info)
        self.__total_duration = datetime.timedelta(seconds=0)
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.title = self.playlist_info['items'][0]['snippet']['title']

    @property
    def total_duration(self):
        video_ids = [video['contentDetails']['videoId'] for video in self.playlist_info['items']]
        video_response = PlayList.youtube.videos().list(part='contentDetails',
                                               id=','.join(video_ids)
                                               ).execute()
        print(video_response)
        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            video_duration = isodate.parse_duration(iso_8601_duration)
            self.__total_duration += video_duration
        return self.__total_duration


if __name__ == '__main__':

    some = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    duration = some.total_duration
    print(duration)
    print(some.playlist_info)
