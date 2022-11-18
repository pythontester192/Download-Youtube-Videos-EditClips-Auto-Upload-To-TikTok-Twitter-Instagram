from pytube import YouTube
from moviepy.editor import *
import requests, os
from PIL import Image

yt_link = "https://www.youtube.com/shorts/QJ28d7KFwvY" #Add your prefered youtube video link here

video = YouTube(yt_link)

#Extract Title
video_title = video.title  

#Extract Thumbnail Link
video_thumbnail = video.thumbnail_url       

#Download Youtube Video
downloaded_video = video.streams.filter(file_extension='mp4').get_highest_resolution().download()
os.rename(downloaded_video, "downloaded_video.mp4")

#Extract Clip Duration
clip = VideoFileClip("downloaded_video.mp4")
clip_duration = clip.duration

#Generate a text clip
txt_clip = TextClip("Link in Bio!", fontsize = 70, color = 'black')    
txt_clip = txt_clip.set_pos('top').set_duration(clip_duration)

#Adding Color Effect to the clip
# clip = clip.fx( vfx.colorx, 2.5)

#Export Final Video Clip & Save It in Media Folder
final_video = CompositeVideoClip([clip, txt_clip])
final_video = final_video.write_videofile("media/final_video.mp4")

if os.path.exists("downloaded_video.mp4"):
  os.remove("downloaded_video.mp4")
else:
  print("The video does not exist")

#Saving Thumbnail in Media Folder
img = Image.open(requests.get(video_thumbnail, stream = True).raw)
img.save("media/thumbnail.jpg")

#Printing The Results
print("{} ----YT Video Downloaded Successfully!".format(video_title))