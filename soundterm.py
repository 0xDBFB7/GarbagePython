import math
import numpy as np
import sounddevice as sd
from time import sleep

wave_dict = [{"freq":300.0,"amp":0.5,"phase":0.0,"LFO_freq": 0.1,"LFO_phase":0.0,"LFO_F":0.5,"LFO_A":0.0,"LFO_P":0}]
# wave_dict = [{"freq":300.0,"amp":0.5,"phase":0.0,"LFO_freq": 0.1,"LFO_phase":0.0,"LFO_F":0.5,"LFO_A":0.0,"LFO_P":0},{"freq":1000.0,"amp":0.5,"phase":0.0,"LFO_freq": 0.1,"LFO_phase":0.0,"LFO_F":1.0,"LFO_A":0.0,"LFO_P":0},{"freq":200.0,"amp":1.0,"phase":0.0,"LFO_freq": 0.1,"LFO_phase":0.0,"LFO_F":0.0,"LFO_A":1.0,"LFO_P":0},{"freq":600.0,"amp":0.5,"phase":2.0,"LFO_freq": 1.0,"LFO_phase":0.0,"LFO_F":0.0,"LFO_A":1.0,"LFO_P":0},{"freq":310.0,"amp":0.5,"phase":1.0,"LFO_freq": 0.5,"LFO_phase":0.0,"LFO_F":0.0,"LFO_A":1.0,"LFO_P":1.0}]


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
    input_array = []
    for i in range(t,int(48000*30)+t):
        amplitude = 0.0
        for wave in wave_dict:
            LFO_amp = math.sin((i*wave["LFO_freq"])/7000.0+wave["LFO_phase"])
            amplitude += math.sin((i*(wave["freq"]+(LFO_amp*wave["LFO_F"])))/7000.0+(wave["phase"]+(LFO_amp*wave["LFO_P"])))*(wave["amp"]+(LFO_amp*wave["LFO_A"]))
        input_array.append(amplitude)
    array = np.array(input_array)
    sd.wait()
    sd.play(array,48000)
    t+=480000*1
