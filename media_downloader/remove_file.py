import os 

os.chdir('C:\\Users\\asus\\Desktop\\media_download\\media_downloader\\test_download')
for files in os.listdir('C:\\Users\\asus\\Desktop\\media_download\\media_downloader\\test_download'):
    if files.endswith('.mp3'):
        os.remove(files)
        print(f"{files} Deleted")
    
    if files.endswith('.mp4'):
        os.remove(files)
        print(f"{files} Deleted")
    
