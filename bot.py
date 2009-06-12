#!/usr/bin/env python

import cPickle as pickle
import os
from datetime import datetime
from urllib import urlopen

from message_queue import MessageQueue
from message import MessageContainer

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
            print "Enqueuing Messages Since Msg#%s UTC" % since

        self.__SaveQueue()

    def PostQueue(self):
        if (self._queue == None):
            self.__LoadQueue()

        # Process messages in queue that have not been retweeted yet

        self.__SaveQueue()

    def __LoadQueue(self):
        if (os.access("%s.mq" % self._hashtag, os.F_OK)):
            self._queue = pickle.load(open("%s.mq" % self._hashtag))
        else:
            self._queue = MessageQueue()

    def __SaveQueue(self):
        pickle.dump(self._queue, open("%s.mq" % self._hashtag, "w"))
