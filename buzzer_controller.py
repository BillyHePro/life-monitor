#! /usr/bin/env python3
# -*- coding: utf-8 -*-
######################################
import RPi.GPIO as GPIO
import time
from heartrate_monitor import HeartRateMonitor
BUZZER_PORT = 11
Tone_CL = [0, 131, 147, 165, 175, 196, 211, 248]
Tone_CM = [0, 262, 294, 330, 350, 393, 441, 495]
Tone_CH = [0, 525, 589, 661, 700, 786, 892, 990]

CUSTOM_SONGS = [
    [Tone_CM[3], Tone_CM[5], Tone_CM[6], Tone_CM[3], Tone_CM[2], Tone_CM[3], Tone_CM[5], Tone_CM[6], Tone_CM[1], Tone_CM[6], Tone_CM[5], Tone_CM[1], Tone_CM[3], Tone_CM[2], Tone_CM[2],
     Tone_CM[3], Tone_CM[5], Tone_CM[2], Tone_CM[3], Tone_CM[3], Tone_CM[6], Tone_CM[6], Tone_CM[6], Tone_CM[1], Tone_CM[2], Tone_CM[3], Tone_CM[2], Tone_CM[7], Tone_CM[6], Tone_CM[1], Tone_CM[5]],
    [Tone_CM[1], Tone_CM[1], Tone_CM[1], Tone_CM[5], Tone_CM[3], Tone_CM[3], Tone_CM[3], Tone_CM[1], Tone_CM[1], Tone_CM[3], Tone_CM[5], Tone_CM[5], Tone_CM[4], Tone_CM[3], Tone_CM[2],
     Tone_CM[2], Tone_CM[3], Tone_CM[4], Tone_CM[4], Tone_CM[3], Tone_CM[2], Tone_CM[3], Tone_CM[1], Tone_CM[1], Tone_CM[3], Tone_CM[2], Tone_CM[5], Tone_CM[7], Tone_CM[2], Tone_CM[1]],
    [Tone_CM[3], Tone_CM[1]]
]

CUSTOM_BEATS = [
    [1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1,
     1, 3, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3],
    [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1,
     3, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 3],
    [1,1]
]


class BuzzerController:
    def __init__(self):
        self.buzz = self.buzzer_setup()
        self.pause()

    def playsong(self, num):
        """
        INPUT song num to play
        """
        self.resume()
        song = CUSTOM_SONGS[num]
        beat = CUSTOM_BEATS[num]
        for i in range(len(song)):
            self.buzz.ChangeFrequency(song[i])
            time.sleep(beat[i]*0.5)
        self.pause()
        
    def pause(self):
        self.buzz.stop()

    def resume(self):
        self.buzz.start(50)

    def buzzer_setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(BUZZER_PORT, GPIO.OUT)
        buzz = GPIO.PWM(BUZZER_PORT, 440)
        buzz.start(50)
        return buzz

    def __del__(self):
        self.buzz.stop()
        GPIO.output(BUZZER_PORT, 1)
        GPIO.cleanup()

buzzer_controller = BuzzerController()


