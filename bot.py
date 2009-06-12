#!/usr/bin/env python

import cPickle as pickle
import os
from datetime import datetime
from urllib import urlopen

from message_queue import MessageQueue
from message import MessageContainer
from search import Search

class TweetBot(object):
    def __init__(self, api, hashtag):
        self._api = api
        self._hashtag = hashtag
        self._queue = None

    def EnqueueNewMessages(self):
        if (self._queue == None):
            self.__LoadQueue()

        since = None
        if (self._queue.last_processed != None):
            since = self._queue.last_processed

        finder = Search(self._hashtag, since)
        for msg in finder.Find():
            self._queue.put(msg)

        self.__SaveQueue()

    def PostMessagesInQueue(self):
        if (self._queue == None):
            self.__LoadQueue()

        for msg in self._queue.queue:
            msg.post(self._api)

        self.__SaveQueue()

    def CleanUpOldMessages(self):
        pass

    def __LoadQueue(self):
        if (os.access("data/%s.mq" % self._hashtag, os.F_OK)):
            self._queue = pickle.load(open("data/%s.mq" % self._hashtag))
        else:
            self._queue = MessageQueue()

    def __SaveQueue(self):
        pickle.dump(self._queue, open("data/%s.mq" % self._hashtag, "w"))
