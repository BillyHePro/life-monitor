#!/usr/bin/env python 3
###############################################
#import necessary library for passing arguments
from heartrate_monitor import HeartRateMonitor
import RPi.GPIO as GPIO
import importlib 
import time
import sys
import argparse

#these are calling relevant library to specific variables
#GPIO NUM
makerobo_Buzz= 11

#LOAD OTHER FUCTIONS
#makerobo_beep=importlib.import_module('09_active_buzzer')


#Lcdfile= importlib.import_module('29_i2c_lcd1602')
#Lcdfile2=importlib.import_module('LCD1602')
Hrcalc=importlib.import_module('hrcalc')
Max30102=importlib.import_module('max30102')
#INIT FUCTIONS
#makerobo_beep.makerobo_setup(makerobo_Buzz)

#Lcdfile.makerobo_setup()
#Lcdfile.makerobo_loop()

#TODO: check further details

# now initialize all libarary for starting up

#set up fundamental variables to judge crtical situations
################

parser = argparse.ArgumentParser(description="Read and print data from MAX30102")
parser.add_argument("-r", "--raw", action="store_true",
                    help="print raw data instead of calculation result")
parser.add_argument("-t", "--time", type=int, default=30,
                    help="duration in seconds to read from sensor, default 30")
args = parser.parse_args()

print('sensor starting...')
hrm = HeartRateMonitor(print_raw=args.raw, print_result=(not args.raw))
hrm.start_sensor()
try:
    time.sleep(args.time)
except KeyboardInterrupt:
    print('keyboard interrupt detected, exiting...')

hrm.stop_sensor()
print('sensor stoped!')

###########
#def makerobo_setup(): 
#    global highbpm, lowbpm, highspo2, lowspo2

#    highbpm=80
#    lowbpm=60
#    highspo2=100
#    lowspo2=80

#ensure other programs are running properly
#def screen():
#    lcd1602.makerobo_setup()
#    makerobo_loop()
#    LCD1602.buzzer_setup()

#now judge critical situations
#if bpm2>=70:
#    buzzerwy  #TODO check further details

#if (bpm2>=60 or bpm2<=100) or (spo22>=85 or spo2<=100):
 #   makerobo_tmp = makerobo_greetings                    # 获取到显示信息
 #   for i in range(0, len(makerobo_greetings)):
        
        
        
        
        # 逐一显示
    #    LCD1602.makerobo_write(0, 0, makerobo_tmp)       # 逐个显示
    #    makerobo_tmp = makerobo_tmp[1:]
    #    time.sleep(0.8)                                  # 延时800ms
     #   LCD1602.makerobo_clear()
     #   LCD1602.makerobo_write(0, 0, 'Enjoy a good life')
    #else:
     #   makerobo_tmp = makerobo_greetings                    # 获取到显示信息
       # for i in range(0, len(makerobo_greetings)):          # 逐一显示
       #     LCD1602.makerobo_write(0, 0, makerobo_tmp)       # 逐个显示
        #    makerobo_tmp = makerobo_tmp[1:]
        #    time.sleep(0.8)                                  # 延时800ms
        #    LCD1602.makerobo_clear()
        #    LCD1602.makerobo_write(0, 0, 'sleep on one side PLZ')
        #    LCD1602.makerobo_write(0, 1, 'To make you heathly')
#def makerobo_loop():
#    while True:
#        ds_temp=90
#        if float(ds_temp)>=60:
#            ds_temp=ds_temp+1
#            for i in range(0,3):     # 播放第一首歌
#                makerobo_beep.makerobo_beep(0.5)
#        if float(ds_temp)<60:
#            for i in range(0,3):     # 播放第一首歌
#               makerobo_beep.makerobo_beep(0.1)
#destroy libraries to debug and amend programs easily and indepentdently 
def makerobo_destroy():
    #LCD1602.destroy()
    #makerobo_beep.destroy()
    heartrate_monitor.stop_sensor()

if __name__ == "__main__":
    try:
    #time.sleep(args.time)
        makerobo_setup()
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destory()
#hrm.stop_sensor()
#print('sensor stoped!')



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