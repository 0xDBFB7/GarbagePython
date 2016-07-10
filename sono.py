import visa
import serial
import msvcrt
from time import sleep
ser = serial.Serial('COM4',57600)
f = open('./amp.txt','a')
ser.write(b':r1c\n')
print(ser.readline())
rm = visa.ResourceManager()
rm.list_resources()
inst = rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZA171409236::INSTR')
b=bytes(':s1f' + str(2280000) + '\n','ascii')
ser.write(b)
sleep(1)
b=bytes(':s1a' + str(500) + '\n','ascii')
ser.write(b)
maxvpp=0
freq = 0
inst.write(':MEASure:SOUR CHAN1')
for i in range(2275000,2310000,100):
    b=bytes(':s1f' + str(i) + '\n','ascii')
    ser.write(b)
    sleep(0.005)
    amplitude = inst.query_ascii_values(':MEASure:VPP?', converter='f')[0]
    if(amplitude > maxvpp):
        maxvpp = amplitude
        freq = i
power = 130
if(maxvpp > 2.6):
    print('Water improperly degassed. Max vpp of ' + str(maxvpp))
sleep(1)
b=bytes(':s1a' + str(power) + '\n','ascii')
ser.write(b)
sleep(1)
b=bytes(':s1f' + str(freq) + '\n','ascii')
ser.write(b)
print('Inject bubble now.') 
sleep(10);
print('Raising to amplitude:')
maintain = 0
amplitude = inst.query_ascii_values(':MEASure:VPP?', converter='f')[0]
while(1==1):
    power = power + 5
    b=bytes(':s1a' + str(power) + '\n','ascii')
    ser.write(b)
    sleep(0.2)
    if msvcrt.kbhit():
        maintain = inst.query_ascii_values(':MEASure:VPP?', converter='f')[0]
        f.write(str(maintain))
        f.close()
        inst.write(':MEASure:SOUR CHAN2')
        brightness = inst.query_ascii_values(':MEASure:VMAX?', converter='f')[0]
        break
    if(power > 1200):
        break
maintain = inst.query_ascii_values(':MEASure:VPP?', converter='f')[0]
inst.write(':MEASure:SOUR CHAN1')
##while True:
##    amplitude = inst.query_ascii_values(':MEASure:VPP?', converter='f')[0]
##    if(amplitude < maintain):
##        freq=freq+1
##        b=bytes(':s1f' + str(freq) + '\n','ascii')
##        ser.write(b)
##        sleep(1)
##    if(msvcrt.kbhit()):
##        pressed = ord(msvcrt.getch())
##        if(pressed == 80):
##            power = power+1
##            b=bytes(':s1a' + str(power) + '\n','ascii')
##            ser.write(b)
##            sleep(0.1)
##        if(pressed == 72):
##            power = power-1
##            b=bytes(':s1a' + str(power) + '\n','ascii')
##            ser.write(b)
##            sleep(0.1)
##            maintain = inst.query_ascii_values(':MEASure:VPP?', converter='f')[0]
##        if(pressed == 77):
##            freq=freq+1
##            b=bytes(':s1f' + str(freq) + '\n','ascii')
##            ser.write(b)
##            sleep(0.1)
##        if(pressed == 75):
##            freq=freq-1
##            b=bytes(':s1f' + str(freq) + '\n','ascii')
##            ser.write(b)
##            sleep(0.1)
        
        
    
        
