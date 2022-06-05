from __future__ import unicode_literals
import requests
import youtube_dl


def downloadVideo(query):
    # Video Search API
    api_key = 'AIzaSyAv82-QVpxlp7pSY5YUEaI6gEQd8QGnNNc'
    response = requests.get("https://www.googleapis.com/youtube/v3/search?key=" + api_key + "&type=video&part=snippet&maxResults=1" + "&q=" + query)
    print(response.text)
    data = response.json()
    video_id = data['items'][0]['id']['videoId']
    print(video_id)

    # Caption search API
    response = requests.get("https://www.googleapis.com/youtube/v3/captions?key=" + api_key + "&part=snippet" + "&videoId=" + video_id)
    print(response.text)
    data = response.json()
    caption = data['items']
    if(caption):
        print("Caption exists for this video!")
    else:
        print("Captions not found for this video..")

    # Downloading Video via youtube-dl

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + video_id])

    

downloadVideo("5 levels of beethoven")