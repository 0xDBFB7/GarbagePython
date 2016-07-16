from __future__ import division
import math
from easygui import *
import pyaudio as PyAudio # sudo apt-get install python{,3}-pyaudio
from itertools import izip
from time import sleep
import sys
from threading import Thread,Event
import audioop
import struct
from array import array
import pygame
from pygame.locals import *
from pygame.mixer import Sound, get_init, pre_init

class Note(Sound):

    def __init__(self, frequency, volume=.1):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

chunk = 2048
CHANNELS = 1
RECORD_SECONDS = 0.1
frequency = 23000
p = PyAudio.PyAudio()
stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=96000,
                    input=True,
                    output=False,
                    frames_per_buffer=chunk)
pre_init(96000, -16, 1, 1024)
pygame.init()
best_frequency = 0
amplitude = 0




#msgbox(msg="First, I need to tune.", title="", ok_button="Begin!")

for frequency in range(22700,23500,5):
    data=stream.read(6048)
    Note(frequency).stop()
    Note(frequency).play(-1)
    sleep(0.05)
    print(audioop.maxpp(data,2))
    if(audioop.maxpp(data,2) > amplitude):
        amplitude = audioop.maxpp(data,2)
        best_frequency = frequency
frequency = best_frequency
Note(frequency,0.8).play(-1)
print(frequency)
msgbox(msg="Now, inject a bubble.", title="", ok_button="Done!")
volume = 0.1
while(True):
    Note(frequency,volume).play(-1)
    volume = volume+0.05
    sleep(0.1)
    msgbox('Lit')
