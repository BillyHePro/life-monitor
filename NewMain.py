#!/usr/bin/env python 3
###############################################
#import necessary library for passing arguments
from buzzerwy import Buzzer
from heartrate_monitor import HeartRateMonitor
import RPi.GPIO as GPIO
import importlib 
import time
import sys 

#these are calling relevant library to specific variables
buzzergpio= 17
Lcdfile= importlib.import_module('lcd1602')
LcdfileCap=importlib.import_module('LCD1602')
Hrcalc=importlib.import_module('hrcalc')
Max30102=importlib.import_module('max30102')
# now initialize all libarary for starting up, some classes have been declared in
#'import', so no need to initizlize libraries repeatedly.

#set up fundamental variables and initize each program properly. The formal one is used
#to judge critical situations
def setup(): 
    global highbpm, lowbpm, highspo2, lowspo2
    boolbpm=False
    boolspo2=False
    Buzzer.setup()
    Lcdfile.makerobo_setup()
    callValue=HeartRateMonitor()
    currentbpm=callValue.getbpm()
    currentspo2=callValue.getspo2()
    highbpm=80
    lowbpm=60
    highspo2=100
    lowspo2=80

#now judge critical situations
while True:
    Lcdfile.makerobo_loop()
    if bpm2>=70:
        BoolBpm=True    #TODO check further details

if (bpm2>=60 or bpm2<=100) or (spo22>=85 or spo2<=100):
    BoolSpo2=True
    BoolBpm=True
    makerobo_tmp = makerobo_greetings                    # 获取到显示信息
    
#destroy libraries to debug and amend programs easily and indepentdently 
def destroy():
    LCD1602.destroy()
    buzzerwy.buzzer_destroy()
    heartrate_monitor.stop_sensor()


try:
    time.sleep(args.time)
except KeyboardInterrupt:
    print('keyboard interrupt detected, exiting...')
hrm.stop_sensor()
print('sensor stoped!')



'''
while (bpm2>=70):
        for i in range(1, len(song_1)):
            buzz.ChangeFrequency(song_1[i])
            time.sleep(beat_1[i]*0.5)
    
    if (bpm2>=60 or bpm2<=100) or (spo22>=85 or spo2<=100):  
        makerobo_tmp = makerobo_greetings                    # 获取到显示信息
        for i in range(0, len(makerobo_greetings)):          # 逐一显示
            LCD1602.makerobo_write(0, 0, makerobo_tmp)       # 逐个显示
            makerobo_tmp = makerobo_tmp[1:]
            time.sleep(0.8)                                  # 延时800ms
            LCD1602.makerobo_clear()
        LCD1602.makerobo_write(0, 0, 'Enjoy a good life')
    else:
        makerobo_tmp = makerobo_greetings                    # 获取到显示信息
        for i in range(0, len(makerobo_greetings)):          # 逐一显示
            LCD1602.makerobo_write(0, 0, makerobo_tmp)       # 逐个显示
            makerobo_tmp = makerobo_tmp[1:]
            time.sleep(0.8)                                  # 延时800ms
            LCD1602.makerobo_clear()
            LCD1602.makerobo_write(0, 0, 'sleep on one side PLZ')
            LCD1602.makerobo_write(0, 1, 'To make you heathly')
'''