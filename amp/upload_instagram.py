import os
from time import sleep
from clicknium import clicknium as cc, locator,ui

def upload(caption, cover_img_file, video_file):
    tab = cc.chrome.attach_by_title_url(url="https://*instagram.com/*")
    tab.goto("instagram.com/passive_income.py/") #Add your instagram url here
    sleep(3)
    tab.find_element(locator.chrome.instagram.svg_add_post).click()
    sleep(3)
    tab.find_element(locator.chrome.instagram.button_select_file).click(by='mouse-emulation')
    sleep(3)
    ui(locator.chrome.edit_file).set_text(video_file, by='set-text')
    sleep(3)
    ui(locator.chrome.button_open).click(by='control-invocation')
    sleep(3)
    tab.find_element(locator.chrome.instagram.button_next).click()
    sleep(3)
    tab.find_element(locator.chrome.instagram.button_selectfromcomputer).click(by='mouse-emulation')
    sleep(3)
    ui(locator.chrome.edit_file).set_text(cover_img_file, by='set-text')
    sleep(3)
    ui(locator.chrome.button_open).click(by='control-invocation')
    sleep(3)
    tab.find_element(locator.chrome.instagram.button_next).click()
    sleep(3)
    tab.find_element(locator.chrome.instagram.textarea).click(by='mouse-emulation')
    tab.find_element(locator.chrome.instagram.textarea2).set_text(caption)
    sleep(3)
    tab.find_element(locator.chrome.instagram.button_share).click()
    sleep(3)
    tab.wait_appear(locator.chrome.instagram.h2_yourposthasbeenshared, wait_timeout=150)

if __name__ == "__main__":
    cover_image = os.path.join(os.getcwd(), "media", "logo.png")
    video_file = os.path.join(os.getcwd(), "media", "clicknium_introduction.mp4")
    upload('Clicknium introduction', cover_image, video_file)