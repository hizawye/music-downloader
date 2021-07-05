from __future__ import unicode_literals
import youtube_dl
import os

def downl(vurl):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
	    'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': False,
        'outtmpl':f'{os.getcwd()}/%(title)s.%(ext)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(vurl)])
def files():
    arr = os.listdir(f'{os.getcwd()}/music/')
    def loop():
        for i in arr:
            yield i[:-4]
    files = [f for f in loop()]
    return files

if __name__ == "__main__":
    yuvid = input("Enter video url: ")
    downl(yuvid)
