from src.channel import Channel

if __name__ == '__main__':
    vdud = Channel('UCI6JEMLSqgbBKgEZR2zrJNw')
    vdud.print_info()

    """
{
  "kind": "youtube#channelListResponse",
  "etag": "PWpBPq86rNnBbY5GQn5vE5LP_Uo",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "n79EPZDF1sZPiPzyoVUkIshQcMY",
      "id": "UCI6JEMLSqgbBKgEZR2zrJNw",
      "snippet": {
        "title": "Андрей += Пронин",
        "description": "Python канал, полезный для начинающих разработчиков и не только. Собеседования джунов. Общение с коллегами про разработку на python. Без лишней зауми.\n",
        "customUrl": "@andypronin",
        "publishedAt": "2020-11-12T06:53:27.698379Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/1xenW3lc97-cO_09TE8ZmgoNxiSZ9FTDisFAX3OH8w-y0ZqGe-oZzxMMEdEj3yPDMjwXvSfpFKo=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/1xenW3lc97-cO_09TE8ZmgoNxiSZ9FTDisFAX3OH8w-y0ZqGe-oZzxMMEdEj3yPDMjwXvSfpFKo=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/1xenW3lc97-cO_09TE8ZmgoNxiSZ9FTDisFAX3OH8w-y0ZqGe-oZzxMMEdEj3yPDMjwXvSfpFKo=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "Андрей += Пронин",
          "description": "Python канал, полезный для начинающих разработчиков и не только. Собеседования джунов. Общение с коллегами про разработку на python. Без лишней зауми.\n"
        },
        "country": "RU"
      },
      "statistics": {
        "viewCount": "1876753",
        "subscriberCount": "18400",
        "hiddenSubscriberCount": false,
        "videoCount": "184"
      }
    }
  ]
}
    """