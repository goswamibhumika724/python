#findout python pakcage to download youtube video 
import yt_dlp

url = 'https://youtu.be/AETFvQonfV8?si=6SCqXLrYCGPkMOxF'

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  # Save file with video title
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    