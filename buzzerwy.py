#! /usr/bin/env python3
# -*- coding: utf-8 -*-
######################################
import RPi.GPIO as GPIO
import time
from heartrate_monitor import HeartRateMonitor
buzzer=11
Tone_CL= [0,131,147,165,175,196,211,248]
Tone_CM= [0,262,294,330,350,393,441,495]
Tone_CH= [0,525,589,661,700,786,892,990]

song_1=[Tone_CM[3],Tone_CM[5],Tone_CM[6],Tone_CM[3],Tone_CM[2],Tone_CM[3],Tone_CM[5],Tone_CM[6]
       ,Tone_CM[1],Tone_CM[6],Tone_CM[5],Tone_CM[1],Tone_CM[3],Tone_CM[2],Tone_CM[2],Tone_CM[3],Tone_CM[5],Tone_CM[2]
       ,Tone_CM[3],Tone_CM[3],Tone_CM[6],Tone_CM[6],Tone_CM[6],Tone_CM[1],Tone_CM[2],Tone_CM[3]
       ,Tone_CM[2],Tone_CM[7],Tone_CM[6],Tone_CM[1],Tone_CM[5]]

beat_1=[1,1,3,1,1,3,1,1,1,1,1,1,1,1,3,1,1,3,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,3]

song_2=[Tone_CM[1],Tone_CM[1],Tone_CM[1],Tone_CM[5],Tone_CM[3],Tone_CM[3],Tone_CM[3],Tone_CM[1]
       ,Tone_CM[1],Tone_CM[3],Tone_CM[5],Tone_CM[5],Tone_CM[4],Tone_CM[3],Tone_CM[2],Tone_CM[2],Tone_CM[3],Tone_CM[4]
       ,Tone_CM[4],Tone_CM[3],Tone_CM[2],Tone_CM[3],Tone_CM[1],Tone_CM[1],Tone_CM[3],Tone_CM[2]
       ,Tone_CM[5],Tone_CM[7],Tone_CM[2],Tone_CM[1]]

beat_2=[1,1,2,2,1,1,2,2,1,1,2,2,1,1,3,1,2,2,1,1,2,2,1,1,2,2,1,1,1,3]

class Buzzer(self,BoolBpm,BoolSpo2):
    def buzzer_setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(buzzer, GPIO.OUT)
        buzz=GPIO.PWM(buzzer, 440)
        buzz.start(50)
        return buzz

    def buzzer_destroy():
        buzz.stop()
        GPIO.output(buzzer,1)
        GPIO.cleanup()
    
    def __init__(self,BoolBpm,BoolSpo2):
        if BoolBpm==True or BoolSpo2==True:
            buzz = buzzer_setup()
            for i in range(5):
                buzz.ChangeFrequency(song_1[i])
                time.sleep(beat_1[i]*0.5)