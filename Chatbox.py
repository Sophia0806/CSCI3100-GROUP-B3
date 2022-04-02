import math
import pygame

class chatbox:
    def __init__(self):
        self._activated = False
        self._messages = []
    
    def activate(self):
        self._activated = True
        pass
    
    def generate_messages(self):
        if self._activated:
            pass#send message while chatbox is activated
    
    def close(self):
        self._activated = False
        pass
    
    def display(self,Map):
        if self._activated:
            pass

class message:#messages within chatbox
    def __init__(self,content,sender,time):
        self._content = content
        self._sender = sender
        self._time = time
    