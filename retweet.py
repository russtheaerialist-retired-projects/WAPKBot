#!/usr/bin/env python

from twitter import Twitter
from bot import TweetBot
t = Twitter()
# profile = t.account.verify_credentials()

bot = TweetBot(t, "#WAPK")
bot.EnqueueNewMessages()
