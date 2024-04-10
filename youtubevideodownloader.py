

from pytube import YouTube
print("youtube video downloader by vani:)")
n=input("The video you downloading is based on video timing you lose your space in your device also are you agree:")
if n=='yes':
 video=str(input("Video link goes here : "))
 path=input("enter file destination : ")
try:
    YouTube(video).streams.first().download(path)
    print("Downloading")
except:
    print("Unfinished due to errors")  