#!/usr/bin/env python

from Queue import Queue
from datetime import datetime

class MessageQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.last_processed = None

    def __getstate__(self):
       return (self.queue, self.last_processed)

    def put(self, value):
        self.last_processed = max(self.last_processed, value.msgId)
        Queue.put(self, value)

    def __setstate__(self, state):
       Queue.__init__(self)
       self.queue = state[0]
       self.last_processed = state[1]


if __name__ == "__main__":

    import pickle
    import message

    mq = MessageQueue()
    mq.put(message.MessageContainer(1, message.Message("shakes", "test 1", datetime.utcnow())))
    mq.put(message.MessageContainer(2, message.Message("shakes", "test 2", datetime.utcnow())))
    mq.put(message.MessageContainer(3, message.Message("shakes", "test 3", datetime.utcnow())))
    mq.put(message.MessageContainer(4, message.Message("shakes", "test 4", datetime.utcnow())))
    print mq.last_processed,
    print mq.queue

    for y in mq.queue:
        y._username = "newuser"

    print mq.queue
    
    pickle.dump(mq, open("msg.q", "w"))
    mq = None
    print mq

    mq = pickle.load(open("msg.q", "r"))
    print mq.last_processed,
    print mq.queue
