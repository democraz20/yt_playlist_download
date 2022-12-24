import os
import threading
import time
try: 
    from pytube import Playlist, YouTube
except ModuleNotFoundError: 
    print('modules missing, installing them now.')
    os.system("pip install pytube")

def get_playlists(l: list[str]) -> list[str]:
    urls: list[str] = []
    for playlist in l:
        playlist_urls = Playlist(playlist)
        for link in playlist_urls: 
            urls.append(link)
    for link in playlist_urls: 
        urls.append(link)
    return urls

def download(url: str, destination: str, audio_only=False):
    yturl = YouTube(url)
    print(f"downloading {yturl.title}")
    video = yturl.streams.filter(only_audio=audio_only).first()
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(f"downloaded {yturl.title} successfully")

def start_cli():
    urls: list[str] = []
    while True:
        i = str(input("  input playlist url >> "))
        if i != "" :
            urls.append(i)
        else: break
    # location = str(input(' input download location : '))
    print("  Enter the destination (leave blank for current directory)")
    destination = str(input("  >> ")) or '.'
    for url in get_playlists(urls):
        download(url, destination)
    print(urls) 

if __name__ == '__main__':
    # start_gui()
    start_cli()