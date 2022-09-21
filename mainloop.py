#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# －－－－湖南创乐博智能科技有限公司－－－－
#  文件名：29_i2c_lcd_controller.py
#  版本：V2.0
#  author: zhulin
#  说明：IIC lcd_controller液晶显示器模块实验
#####################################################
import lcd_controller   # lcd_controller液晶显示屏库
import time
from buzzer_controller import buzzer_controller
from heartrate_monitor import HeartRateMonitor

# 初始化lcd_controller液晶模块
def lcd_setup():
	lcd_controller.makerobo_init(0x27, 1)	# 初始化(设备地址, 背光设置)
	lcd_controller.makerobo_write(0, 0, 'sensor starting')     # 显示第一行信息
	lcd_controller.makerobo_write(0, 1, 'made by Billy') # 显示第二行信息
	time.sleep(4)

def clear_screen():
	lcd_controller.makerobo_init(0x27, 1)	# 初始化(设备地址, 背光设置)
	lcd_controller.makerobo_write(0, 0, ' '*15)

def write_to_screen(text : str, line:int):
	LINE_SPACE = 16
	if len(text) < 16 :
		text = text +  " " * (16-len(text))
	lcd_controller.makerobo_write(0, line, text) 
	

# 循环函数
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
			

# 释放资源
def destroy():
	clear_screen()
	hrm.stop_sensor()

# 程序入口
if __name__ == "__main__":
	try:
		hrm = HeartRateMonitor(False, True)
		hrm.start_sensor()
		# 开始了线程, 控制线程播放动画
		lcd_setup()      # 初始化信息
		clear_screen()
		main_loop(hrm)       # 循环显示信息

	except KeyboardInterrupt: # 当按下Ctrl+C时，将执行destroy()子程序。
		destroy()             # 释放资源