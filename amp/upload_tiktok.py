import os
from time import sleep
from clicknium import clicknium as cc, locator,ui

def upload(caption, video_file):
    tab = cc.chrome.attach_by_title_url(url="https://www.tiktok.com*")
    tab.goto("tiktok.com/upload?lang=en")
    sleep(3)
    tab.find_element(locator.chrome.tiktok.div).set_focus()
    cc.send_text(caption)
    sleep(3)
    tab.find_element(locator.chrome.tiktok.button_selectfile).click()
    sleep(3)
    ui(locator.chrome.edit_file).set_text(video_file, by='set-text')
    sleep(3)
    ui(locator.chrome.button_open).click(by='control-invocation')
    sleep(3)
    tab.find_element(locator.chrome.tiktok.disable_button).wait_property('disabled', 'false', wait_timeout=150)
    sleep(3)
    tab.find_element(locator.chrome.tiktok.button_post).click()
    sleep(5)


if __name__ == "__main__":
    video_file = os.path.join(os.getcwd(), "media", "clicknium_introduction.mp4")
    upload('Clicknium introduction', video_file)