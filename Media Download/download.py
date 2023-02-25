from pytube import YouTube
import os

def download_video(link,dir):
    os.chdir(dir)
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def yt_audio(link,dir):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=dir)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")

def song(link,dir):
    os.chdir(dir)
    run='spotdl '+link
    os.system(run)

link = input("Enter the YouTube video URL : ")
directory = input("Enter the path where you to save video (press enter if you save in current directory) : ")
option=int(input('Enter option 1:Download Audio 2:Download Video: '))
extact=link.split("/")
site=extact[2]
if option==1:
    if site=='open.spotify.com':
        song(link,directory) #https://open.spotify.com/track/3tjTLJOAc2FFJi2LkHFcXl?si=d81add2eef1f4fd6
    elif site=='www.youtube.com':
        yt_audio(link,directory) #https://www.youtube.com/watch?v=5Eqb_-j3FDA
elif option==2:
    download_video(link,directory) #https://www.youtube.com/watch?v=HbTON0nb4DU
else:
    print("Enter a valid option i.e 1 or 2")