import math
import numpy as np
import sounddevice as sd
from time import sleep
import random
random.seed()

wave_dict = []

# import Tkinter
# from Tkinter import *
# import tkMessageBox
#
# top = Tkinter.Tk()
# top.title("Fourier Synth")
# w = Canvas(top, width=500, height=500)
# w.grid(row=4, column=1,sticky=W)
# top.mainle
t=0
while True:
    wave_dict = []
    melody_speed = random.randint(12000,64000)
    for i in range(0,random.randint(1,10)):
        wave_dict.append({"freq":random.randint(1,2000),"melody_speed": ,"melody":[random.randint(50,200)/100.0],"amp":random.randint(0,100)/100.0,"phase":random.randint(1,314)/100.0,"LFO_freq": random.randint(1,1000)/100.0,"LFO_phase":random.randint(1,314)/100.0,"LFO_F":random.randint(1,100)/100.0,"LFO_A":random.randint(1,100)/100.0,"LFO_P":random.randint(1,314)/100.0})
    input_array = []
    for i in range(t,int(48000*20)+t):
        amplitude = 0.0
        for wave in wave_dict:
            LFO_amp = math.sin((i*wave["LFO_freq"])/7000.0+wave["LFO_phase"])
            amplitude += math.sin((i*(wave["freq"]+(LFO_amp*wave["LFO_F"])))/7000.0+(wave["phase"]+(LFO_amp*wave["LFO_P"])))*(wave["amp"]+(LFO_amp*wave["LFO_A"]))
        input_array.append(amplitude)
    array = np.array(input_array)
    sd.wait()
    sd.play(array,48000)
    t+=480000*1
