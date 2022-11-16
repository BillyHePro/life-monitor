#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################
import lcd_controller   # lcd_controller LCD display library
import time
from buzzer_controller import buzzer_controller
from heartrate_monitor import HeartRateMonitor

# initialize lcd_controller liquid crystal module
def lcd_setup():
	lcd_controller.makerobo_init(0x27, 1)	# initialize device address and backlight setting
	lcd_controller.makerobo_write(0, 0, 'sensor starting')     # display the first line of information
	lcd_controller.makerobo_write(0, 1, 'made by Billy') # display the second line of information
	time.sleep(4)

def clear_screen():
	lcd_controller.makerobo_init(0x27, 1)	# initialize device address and backlight setting
	lcd_controller.makerobo_write(0, 0, ' '*15)

def write_to_screen(text : str, line:int):
	LINE_SPACE = 16
	if len(text) < 16 :
		text = text +  " " * (16-len(text))
	lcd_controller.makerobo_write(0, line, text) 
	

# round function
def main_loop(hrm:HeartRateMonitor):
	while True:
		time.sleep(1)
		bpm = hrm.bpm
		spo2 = hrm.spo2

		write_to_screen("bpm:   " + str(round(hrm.getbpm(),2)), 0)
		write_to_screen("spo2:  " + str(round(hrm.getspo2(),2)), 1)


		danger_cond = bpm >= 120 or spo2 <= 10

		if danger_cond:
			write_to_screen("Warning!", 0)
			write_to_screen("You in danger!", 1)
			buzzer_controller.playsong(2)
			

# release resources
def destroy():
	clear_screen()
	hrm.stop_sensor()

# program entry
if __name__ == "__main__":
	try:
		hrm = HeartRateMonitor(False, True)
		hrm.start_sensor()
		# start the thread, control the thread to play the animation
		lcd_setup()      # initialize information
		clear_screen()
		main_loop(hrm)       # Cycle through information

	except KeyboardInterrupt: # When Ctrl+C is pressed, the destroy() subroutine will be executed.
		destroy()             # release resources
