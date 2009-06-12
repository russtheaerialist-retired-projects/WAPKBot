#!/usr/bin/env python

import os

class _Config:
    def __init__(self):
        self._username = "NerdsInShape"
        self._password = None

    def get_username(self):
        return self._username
    username = property(get_username)

    def get_password(self):
        if (not self._password):
            self._password = self.__load_password()
        return self._password
    password = property(get_password)

    def __load_password(self):
        if (os.access(".pass.txt", os.F_OK)):
            return open(".pass.txt", "r").readline().strip()
        else:
            return ""

Config = _Config()
