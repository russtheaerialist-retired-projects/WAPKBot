#!/usr/bin/env python

from urllib import urlopen, urlencode
from message import Message, MessageContainer
from config import Config
import simplejson

class Search:
    def __init__(self, hashtag, since = None):
        self._hashtag = hashtag
        self._since = since

    def __create_url(self):
        query = { 'q': self._hashtag, 'rpp': 100, 'show_user': False }
        if (self._since):
            query['since_id'] = self._since

        url = "http://search.twitter.com/search.json?%s" % urlencode(query)

        return url

    def Find(self):
        url = self.__create_url()
        conn = urlopen(url)
        retval = simplejson.load(conn)
        for msg in retval['results']:
            container = MessageContainer(msg['id'])
            if (container.inner == None):
                container.inner = msg
            if (not container.was_retweeted and
                    container.username.upper() != Config.username.upper()):
                yield container


if __name__ == '__main__':
    x = Search("#WAPK")
    print x.Find()
