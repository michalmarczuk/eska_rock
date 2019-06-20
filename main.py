#!/usr/bin/python3
# vim: set encoding=utf-8


import tkinter
from tkinter import PhotoImage
from functools import partial

from current_song import CurrentSong
from logger import Logger
from play_stop_button import PlayStopButton
from window_with_logo import WindowWithLogo


BACKGROUND_COLOR = "grey12"

window = WindowWithLogo()

logo_image = PhotoImage(file="images/eska_logo.png")
logo = tkinter.Label(window, image=logo_image, bg=BACKGROUND_COLOR)
logo.photo = logo_image
logo.grid(row=0)

play_stop_button = PlayStopButton(window)
play_stop_button.grid(row=1, column=0, sticky=tkinter.W, padx=(15, 15), pady=(15, 15))

logging_label = tkinter.Label(window, text="tra la la la la la la la la la ")
logging_label.grid(row=2, column=0, pady=(20, 0))
Logger.get_instance().logging_label = logging_label

frame = tkinter.Frame(window)
frame.configure(background=BACKGROUND_COLOR)
frame.grid(row=1, column=0, padx=(100, 10))
wait_30_button = tkinter.Button(frame, text="30 sekund")
wait_30_button.grid(row=0, column=0, pady=(5, 5))
wait_60_button = tkinter.Button(frame, text="60 sekund")
wait_60_button.grid(row=1, column=0, pady=(5, 5))
wait_90_button = tkinter.Button(frame, text="90 sekund")
wait_90_button.grid(row=2, column=0, pady=(5, 5))

# window.after(5000, lambda: frame.grid_forget())
# window.after(10000, lambda: frame.grid(row=1, column=0, padx=(100, 10)))

# timer_label = tkinter.Label(window, text="0")


def song_info():
    CurrentSong.get()
    window.after(10000, lambda: song_info())


def timer(counter: int):
    frame.grid_forget()
    minutes = str(int(counter / 60)).zfill(2)
    seconds = str(counter % 60).zfill(2)
    timer_label = tkinter.Label(window, text=f"{minutes}:{seconds}")
    timer_label.grid(row=1, column=0, padx=(100, 5))

    new_value = counter - 1

    if new_value >= 0:
        window.after(1000, timer, new_value)
        window.after(1000, lambda: timer_label.destroy())
    else:
        window.after(1000, lambda: timer_label.destroy())
        window.after(1200, lambda: frame.grid(row=1, column=0, padx=(100, 10)))


# window.after(1000, timer)
wait_30_button.config(command=partial(timer, 30))
wait_60_button.config(command=partial(timer, 60))
wait_90_button.config(command=partial(timer, 90))


window.after(10000, lambda: song_info())

window.mainloop()

print(tkinter.TkVersion)
