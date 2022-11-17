import os
from time import sleep
from clicknium import clicknium as cc, locator,ui

def upload(tweet, video_file):
    tab = cc.chrome.attach_by_title_url(url="https://*twitter.com/*")
    tab.goto("twitter.com/compose/tweet")
    sleep(3)
    tab.find_element(locator.chrome.twitter.div).set_focus()
    cc.send_text(tweet)
    sleep(3)
    tab.find_element(locator.chrome.twitter.svg).click()
    sleep(3)
    ui(locator.chrome.edit_file).set_text(video_file, by='set-text')
    sleep(3)
    ui(locator.chrome.button_open).click(by='control-invocation')
    sleep(3)
    tab.wait_appear(locator.chrome.twitter.video)
    sleep(3)
    tab.find_element(locator.chrome.twitter.span_tweet).click()
    sleep(5)

if __name__ == "__main__":
    video_file = os.path.join(os.getcwd(), "media", "short_introduction.mp4")
    upload('Clicknium introduction', video_file)