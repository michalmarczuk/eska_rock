#!/usr/bin/python3
# vim: set encoding=utf-8

import os
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

ESKA_URL = "http://www.eskago.pl/radio/eska-rock"


class Player:

    def __init__(self):
        self.url = None
        os.environ['MOZ_HEADLESS'] = '1'
        self.browser = None

    def get_url(self):
        self.browser = webdriver.Firefox()
        self.browser.get(ESKA_URL)

        # Wait until page loaded
        url = None
        attempt = 0

        while url is None:
            try:
                print("Trying to get url")
                url = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "video"))).get_attribute('src')
            except TimeoutException:
                attempt += 1
                print(f"Retrying to get url({attempt})")
                if attempt > 2:
                    print("Refreshing page")
                    self.browser.refresh()

        print(url)

        self.url = url

    def play(self):
        if not self.url:
            self.get_url()

        self.browser.get(self.url)

    def stop(self):
        self.browser.quit()
        self.url = None
