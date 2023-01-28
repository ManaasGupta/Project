from pytube import YouTube
import argparse
import os
import sys
import imageio


def download(args):
    os.makedirs(args.dir,exist_ok=True)
    os.chdir(args.dir)
    youtube_object=YouTube(args.link)
    youtube_objects=youtube_object.streams.get_highest_resolution()
    youtube_object=youtube_object.title
    youtube_objects.download()  
    os.chdir(args.dir)
    a=os.listdir(args.dir)
    print(a)
    file_name=a[-1]
    print(file_name)
    file_path=args.dir+'\\'+file_name
    print(file_path)
    reader = imageio.get_reader(file_name)
    frame = reader.get_data(0)
    height=frame.shape[0]
    width=frame.shape[1]
    resolution={
    144:'144p',
    240:'240p',
    480:'SD',
    720:'HD',
    1080:'Full HD',
    1440:'2K',
    2160:'4K',
    4320:'8K'
    }
    if height in resolution:
        reso=resolution[height]
    return f'\n{youtube_object}.mp4 video downloaded \n\nDimension {width} X {height} \n\nResolution is {reso} \n'


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--link',type=str, help="link of video in youtube",required=True)
    parser.add_argument('--dir',type=str, help='enter the abs,relative path where you want to audio_files',default='C:\\Users\\asus\\Desktop\\media_download\\media_downloader\\test_download')
    args=parser.parse_args()
    sys.stdout.write(str(download(args)))