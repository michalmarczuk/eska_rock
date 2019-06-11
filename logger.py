#!/usr/bin/python3
# vim: set encoding=utf-8

import logging


class Logger:
    __instance = None

    @staticmethod
    def get_instance() -> "Logger":
        if Logger.__instance is None:
            Logger()

        return Logger.__instance

    def __init__(self):
        if Logger.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger.__instance = self

        logging.getLogger().setLevel(logging.INFO)
        logging.basicConfig(filename="eska_rock.log", format="%(asctime)s %(message)s", filemode="a")

        self.__logging_label = None

    @property
    def logging_label(self):
        return self.__logging_label

    @logging_label.setter
    def logging_label(self, logging_label):
        self.__logging_label = logging_label

    def info(self, message: str):
        logging.info(message)

        if self.__logging_label is not None:
            self.__logging_label.configure(text=message)
            self.__logging_label.master.update()
