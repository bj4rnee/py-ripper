from pytube import YouTube

url = ""
yt = YouTube(url)

yt_stream = yt.streams.get_highest_resolution() # TODO audio only
print("[Debug] Downloading " + url + " ...")
yt_stream.download() # TODO args