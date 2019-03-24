import os
import re
import tkinter
import vlc
import urllib.request
from tkinter import *

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

ESKA_URL = "http://www.eskago.pl/radio/eska-rock"


def radio_url() -> str:
    # os.environ['MOZ_HEADLESS'] = '1'
    browser = webdriver.Firefox()
    browser.get(ESKA_URL)

    # Wait until page loaded
    url = None
    attempt = 0

    while url is None:
        try:
            print("Trying to get url")
            url = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "video"))).get_attribute('src')
        except TimeoutException:
            attempt += 1
            print(f"Retrying to get url({attempt})")
            if attempt > 2:
                print("Refreshing page")
                browser.refresh()

    browser.quit()
    print(url)

    return url


def application(window):

    p = vlc.MediaPlayer(radio_url())
    p.play()
    # window.quit()


top = tkinter.Tk()
top.title("Czekam aż Eska Rock się załaduje...")
top.after(500, application, top)

photo = PhotoImage(file="waiting_dog.gif")
label = Label(top, image=photo)
label.image = photo
label.pack()

# Hack for Mac - maximalize window
top.attributes('-topmost', 1)
top.update()
top.mainloop()
