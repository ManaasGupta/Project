import eyed3
import os
from pathlib import Path

path="C:\\Users\\asus\\Desktop\\media_download\\media_downloader\\test_download"
os.chdir('C:\\Users\\asus\\Desktop\\media_download\\media_downloader\\test_download')
paths =sorted(Path(path).iterdir(), key=os.path.getmtime)
last_file=paths[-1]
print(last_file)
# meta_data=audio_metadata.load(last_file)
# print(meta_data)


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
print(info_dict)
