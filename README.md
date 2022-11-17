# Free BOT Money Maker Using Python & Clicknium

## Tutorial Videos on How to Use Clicknium
Open media folder, where you can find 3 basic videos on how to set up Clicknium module, & how to use it step by step.

## Run Python Code
- follow [clicknium getting started](https://www.clicknium.com/documents/quickstart) to set up develop environment.
- install the required libraries before running this bot.
```
pip install -r requirements.txt
```
- run `python generate_video.py` to download yt video and edit the clip with moviepy library.
- open `main.py`.
- open the chrome browser (guarantee that there is only one chrome window, explained later), open 3 tabs respectively, open and login TikTok, Twitter and Instagram.
- press `F5` to debug the sample or press `CTRL+F5` to run the main file.
```python
caption = 'Write your video title here'
cover_image = os.path.join(os.getcwd(), "media", "thumbnail.jpg")
video_file = os.path.join(os.getcwd(), "media", "final_video.mp4")
upload_tiktok.upload(caption, video_file)
upload_twitter.upload(caption, short_video_file)
upload_instagram.upload(caption, cover_image, video_file)
```

## Watch This Full Tutorial Video on How to Use This GitHub Project
- Follow Step By Step This [Youtube Video Tutorial](https://www.youtube.com/c/PythonPassiveIncome)
