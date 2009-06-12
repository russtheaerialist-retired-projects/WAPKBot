#!/usr/bin/env python

from datetime import datetime
import cPickle as pickle
import os

class Message(object):
    def __init__(self, username, message, tweeted_at, retweeted_at = None):
        self._username = username
        self._message = message
        self._tweeted_at = tweeted_at
        self._retweeted_at = retweeted_at

    def __getinitargs__(self):
        return (self._username, self._message, self._tweeted_at,
                self._retweeted_at)

    def post(self, twit):
        if (self._retweeted_at == None):
            twit.statuses.update(status="%s" % self)
            self._retweeted_at = datetime.utcnow()
        return True

    def __str__(self):
        return "(@%s) %s" % (self._username, self._message)

    def __repr__(self):
        return "<Message: %s>" % self

class MessageContainer(object):
    def __init__(self, msgId, message = None):
        self.__msgId = msgId
        self.__message = message

    def get_msgId(self):
        return self.__msgId
    msgId = property(get_msgId)

    def get_inner(self):
        if self.__message == None and os.access(self.filename, os.F_OK):
            self.__load_message()
        return self.__message 
    def set_inner(self, value):
        self.__parse_twitter(value)
        self.__save_message()
    inner = property(get_inner, set_inner)

    def get_username(self):
        return self.inner._username
    username = property(get_username)

    def get_message(self):
        return self.inner._message
    message = property(get_message)

    def get_tweeted_at(self):
        return self.inner._tweeted_at
    tweeted_at = property(get_tweeted_at)

    def _check_retweeted_at(self):
        return self.inner._retweeted_at != None
    was_retweeted = property(_check_retweeted_at)

    def post(self, twit):
        if (self.inner.post(twit)):
            self.__save_message()

    def __create_filename(self):
        return "data/%s.msg" % self.msgId
    filename = property(__create_filename) 

    def __parse_twitter(self, value):
        screenname = value["from_user"]
        message = value["text"]
        tweeted = value["created_at"]
        self.__message = Message(screenname, message, tweeted)
        self.__msgId = value["id"]

    def __load_message(self):
        self.__message = pickle.load(open(self.filename, "r"))

    def __save_message(self):
        pickle.dump(self.__message, open(self.filename, "w"))

    def __str__(self):
        return "%s" % self.inner
