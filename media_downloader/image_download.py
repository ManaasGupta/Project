import requests as rq
import os
import pathlib
import argparse
import sys
import PIL
from PIL import Image

def dl_img(args):#dir_name,file_name,url
    img_source=rq.get(args.link)
    global output
    suffix=pathlib.Path(args.link).suffix
    if suffix not in ['.jpg','.jpeg','.png','.gif']:
        output=args.name+'.png'
    else:
        output=args.name+suffix
    
    os.makedirs(args.dir,exist_ok=True)
    os.chdir(args.dir)
    with open (f"{args.dir}{output}",'wb')as file:
        file.write(img_source.content)
    
    get_reso(args.dir,output)
    return f'Downlaod Sucessful {output}'

def get_reso(dir_name,file_with_estension):
    img = PIL.Image.open(f"{dir_name}\\{file_with_estension}")
    wid, hgt = img.size
    return f"Resolution of image {file_with_estension} is {wid} X {hgt}"




if __name__ =='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--link',type=str, help="link of video in youtube",required=True)
    parser.add_argument('--dir',type=str, help='enter the abs,relative path where you want to audio_files',default='C:\\Users\\asus\\Desktop\\media_download\\media_downloader\\test_download')
    parser.add_argument('--name',type=str,help='Enter the prefix file_name',required=True)
    args=parser.parse_args()
    sys.stdout.write(str(dl_img(args)))
    print('\n')
    sys.stdout.write(str(get_reso(args.dir,output)))
    
