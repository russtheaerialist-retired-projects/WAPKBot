#!/usr/bin/env python

from urllib import urlopen, urlencode
from message import Message, MessageContainer
import simplejson

class Search:
    def __init__(self, hashtag, since = None):
        self._hashtag = hashtag
        self._since = since

    def __create_url(self):
        query = { 'q': self._hashtag }
        if (self._since):
            query['since_id'] = self._since

        url = "http://search.twitter.com/search.json?%s" % urlencode(query)

        return url

    def Find(self):
        url = self.__create_url()
        conn = urlopen(url)
        retval = simplejson.load(conn)
        return retval


if __name__ == '__main__':
    x = Search("#WAPK")
    print x.Find()
