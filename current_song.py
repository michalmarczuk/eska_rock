#!/usr/bin/python3
# vim: set encoding=utf-8
import json
import re

import requests

from logger import Logger
from player import Player


class CurrentSong:
    __instance = None
    __song = ""
    __session = None

    def __init__(self):
        if CurrentSong.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CurrentSong.__instance = self

    @staticmethod
    def get():
        if not Player.get_instance().is_playing():
            return

        song = CurrentSong.__get_instance().__song
        current_song = CurrentSong.__current_song()

        if song != current_song:
            Logger.get_instance().info(current_song)
            CurrentSong.__get_instance().__song = current_song

    @staticmethod
    def __get_instance() -> "CurrentSong":
        if CurrentSong.__instance is None:
            CurrentSong()

        return CurrentSong.__instance

    @staticmethod
    def __current_song() -> str:
        if CurrentSong.__session is None:
            CurrentSong.__session = requests.session()

        response_body = CurrentSong.__session.get("https://static.eska.pl/m/playlist/combine.jsonp?callback=jsonp").text
        stripped_response_body = re.search(r"jsonp\((.*)\);", response_body).group(1)
        response_json = json.loads(stripped_response_body)

        song_name = response_json["108"]["songs"][0]["name"]
        song_artist = response_json["108"]["songs"][0]["artists"][0]["name"]

        return f"{song_artist}: {song_name}"
