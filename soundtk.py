import math
import numpy as np
import sounddevice as sd
from time import sleep

import Tkinter
from Tkinter import *
import tkMessageBox

top = Tkinter.Tk()
top.title("Fourier Synth")
w = Canvas(top, width=500, height=50)
w.grid(row=4, column=1,sticky=W)

wave_dict = [{"freq":1000.0,"amp":1.0,"phase":0},{"freq":1010.0,"amp":1.0,"phase":0}]

display_percentage.configure(text=str(((frequency-(set_frequency-50))))+"% Fine")
e = Tkinter.Button(top, text ="Cancel", command=lambda *args:  ButtonBack('exit'))
e.grid(row=1, column=4)

while True:
    input_array = []
    for i in range(0,int(48000*100)):
        amplitude = 0.0
        for wave in wave_dict:
            amplitude += math.sin((i*wave["freq"])/7000.0+wave["phase"])*wave["amp"]
        input_array.append(amplitude)
    array = np.array(input_array)
    #sd.wait()
    sd.play(array,48000)
    #sd.wait()
