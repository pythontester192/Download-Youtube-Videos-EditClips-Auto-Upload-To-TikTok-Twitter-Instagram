import os
import amp.upload_instagram as upload_instagram
import amp.upload_tiktok as upload_tiktok
import amp.upload_twitter as upload_twitter

caption = 'How to Beat Food Cravings, Lose Weight and Gain Energy' #Describe Your Video Topic
cover_image = os.path.join(os.getcwd(), "media", "thumbnail.jpg")   #The Path of The Thumbnail Image
video_file = os.path.join(os.getcwd(), "media", "final_video.mp4")  #The Path of The Final Video
upload_tiktok.upload(caption, video_file)
upload_twitter.upload(caption, video_file)
upload_instagram.upload(caption, cover_image, video_file)