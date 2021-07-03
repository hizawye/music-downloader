import youtube_dl
from dl_music import downl,files
import re

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})
video = input("Enter playlist url: ")
with ydl:
    result = ydl.extract_info(video,
                    download=False) #We just want to extract the info

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries']

        #loops entries to grab each video_url
        for i, item in enumerate(video):
            video = result['entries'][i]['webpage_url']

            title_wrong = result['entries'][i]['title']

            title = [i[:8] for i in files()]
            if title_wrong[:8] in title:
                continue
            else :
                downl(video)
