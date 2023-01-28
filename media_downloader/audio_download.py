import os
from urllib.parse import urlparse
import pafy
import sys
import argparse
import eyed3
from pathlib import Path

import audio_metadata

# https://open.spotify.com/track/5yIiXdLRE85OBiQmCaUenq?si=e5bef8121728403f
def get_audio(args):
    url = urlparse(args.link).netloc
    link=str(args.link)
    print(url) # --> www.example.test
    os.makedirs(args.dir,exist_ok=True)
    os.chdir(args.dir)

    if url.endswith('youtube.com'):
        # To downlaod audio from
        video = pafy.new(link)
        bestaudio = video.getbestaudio()
        bestaudio.download()
    else:
        #To downlaod songs from sportify
        os.system("spotdl {}".format(link))
    
    paths =sorted(Path(args.dir).iterdir(), key=os.path.getmtime)
    last_file=paths[-1]
    print(last_file)
    audio=eyed3.load(last_file)
    info_dict={
    "Title":audio.tag.title,
    "Artist":audio.tag.artist,
    "Album":audio.tag.album,
    "Album artist":audio.tag.album_artist,
    "Composer":audio.tag.composer,
    "Publisher":audio.tag.publisher,
    "Genre":audio.tag.genre.name
    }
    
    return f"Audio_File Downlaoded with {info_dict}"
if __name__ =='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--link',type=str, help="link of video in youtube",required=True)
    parser.add_argument('--dir',type=str, help='enter the abs,relative path where you want to audio_files',default='C:\\Users\\asus\\Desktop\\media_download\\media_downloader\\test_download')
    args=parser.parse_args()
    sys.stdout.write(str(get_audio(args)))
    