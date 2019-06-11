#!/usr/bin/python3
# vim: set encoding=utf-8

import os
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from logger import Logger

ESKA_URL = "http://www.eskago.pl/radio/eska-rock"


class Player:

    def __init__(self):
        self.url = None
        os.environ['MOZ_HEADLESS'] = '1'
        self.browser = None

    def get_url(self):
        Logger.get_instance().info("Otwieram przeglądarkę")
        self.browser = webdriver.Firefox()
        Logger.get_instance().info('Wchodzę na "http://www.eskago.pl/radio/eska-rock"')
        self.browser.get(ESKA_URL)

        # Wait until page loaded
        url = None
        attempt = 0

        while url is None:
            try:
                Logger.get_instance().info("Szukam adresu do radia na stronie")
                url = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "video"))).get_attribute('src')
            except TimeoutException:
                attempt += 1
                Logger.get_instance().info(f"Szukam adresu do radia na stronie({attempt})")
                if attempt > 2:
                    Logger.get_instance().info("Odświeżam stronę")
                    self.browser.refresh()

        Logger.get_instance().info(f"Znalazłem adres radia: {url}")
        self.url = url

    def play(self):
        if not self.url:
            self.get_url()

        Logger.get_instance().info("Otwieram radio w przeglądarce")
        self.browser.get(self.url)
        Logger.get_instance().info("Odtwarzam radio!")

    def stop(self):
        Logger.get_instance().info("Zamykam przeglądarkę")
        self.browser.quit()
        self.url = None
