#!/usr/bin/env python

from twitter import Twitter
from bot import TweetBot
from config import Config
t = Twitter(Config.username, Config.password)
profile = t.account.verify_credentials()

bot = TweetBot(t, ("#WAPK", "#PNWPA", "#NerdsInShape"))
bot.EnqueueNewMessages()
bot.PostMessagesInQueue()
bot.CleanUpOldMessages()
