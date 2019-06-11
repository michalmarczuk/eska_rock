#!/usr/bin/python3
# vim: set encoding=utf-8

import tkinter


WINDOW_WIDTH = 320
WINDOW_HEIGHT = 420
BACKGROUND_COLOR = "grey12"


class WindowWithLogo(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Eska Rock Player")
        self.configure(background=BACKGROUND_COLOR)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+"
                        f"{int(self.winfo_screenwidth() / 2 - WINDOW_WIDTH / 2)}+"
                        f"{int(self.winfo_screenheight() / 2 - WINDOW_HEIGHT / 1.5)}")
