import math
import numpy as np
import sounddevice as sd
from time import sleep
import random
import pygame
random.seed()
speed = 48000/4
test = pygame.image.load("test.png")
input_array = []
picture = []
for x in range(30):
    for y in range(19):
        picture.append(test.get_at((x,y)).g)

for idx in range(0,48000):
    amplitude = 0.0
    amplitude += math.sin(idx*500.0+(50.0*(picture[idx/speed]/255.0))/7000.0)
    input_array.append(amplitude)
array = np.array(input_array)

while True:
    sd.play(array,48000)
    sd.wait()
    sleep(10)
