#!/usr/bin/env python

import message
import cPickle as pickle
import os

def print_entry(entry):
    msg = message.MessageContainer(entry)
    if (not msg.was_retweeted):
        print msg

if __name__ == "__main__":
    files = os.listdir("data")
    for f in files:
        if (f[-3:] == "msg"):
            print_entry(f.replace(".msg", ""))
