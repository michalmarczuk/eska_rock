#!/usr/bin/python3
# vim: set encoding=utf-8

import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from logger import Logger

ESKA_URL = "http://www.eskago.pl/radio/eska-rock"


class Player:
    __instance = None

    def __init__(self):
        if Player.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.url = None
            os.environ['MOZ_HEADLESS'] = '1'
            self.browser = None
            self.__is_playing = False
            Player.__instance = self

    @staticmethod
    def get_instance() -> "Player":
        if Player.__instance is None:
            Player()

        return Player.__instance

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

    def is_playing(self) -> bool:
        return self.__is_playing

    def play(self):
        if not self.url:
            self.get_url()

        Logger.get_instance().info("Otwieram radio w przeglądarce")
        self.browser.get(self.url)
        Logger.get_instance().info("Odtwarzam radio!")
        self.__is_playing = True

    def stop(self):
        Logger.get_instance().info("Zamykam przeglądarkę")
        self.browser.quit()
        self.url = None
        self.__is_playing = False
