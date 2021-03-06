#!/usr/bin/python3
# vim: set encoding=utf-8

import tkinter
from functools import partial
from tkinter import PhotoImage

from player import Player


class PlayStopButton(tkinter.Button):
    def __init__(self, parent):
        self.play_image = PhotoImage(file="images/play.png")
        self.stop_image = PhotoImage(file="images/stop.png")

        super().__init__(
            parent,
            height=96,
            width=96,
            command=partial(self.play_stop_icon_change, self.stop_image),
            image=self.play_image)

    def play_stop_icon_change(self, image: PhotoImage):
        self.configure(command=partial(self.play_stop_icon_change, self["image"]), image=image)
        self.master.update()

        if self.play():
            Player.get_instance().stop()
        if not self.play():
            Player.get_instance().play()

    def play(self) -> bool:
        return str(self["image"]) == str(self.play_image)
