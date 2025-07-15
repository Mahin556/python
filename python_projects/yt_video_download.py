from pytube import YouTube
import pyshorteners

url = input("Enter a URL:- ").strip()

clean_url = url.split('?')[0]  # removes the ?si=... part

urls=clean_url

vid = YouTube(urls)

video_download = vid.streams.get_highest_resolution()
audio_download = vid.streams.get_audio_only()

entry = YouTube(urls).title

print(f"\nVideo found: {entry}\n")

print(f"Downloading Video...")
video_download.download(filename=f"{entry}.mp4")

print("Downloading Audio...")
audio_download.download(filename=f"{entry}.mp3")

print("Program Completed")