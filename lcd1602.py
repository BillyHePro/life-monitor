#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# －－－－湖南创乐博智能科技有限公司－－－－
#  文件名：29_i2c_lcd1602.py
#  版本：V2.0
#  author: zhulin
#  说明：IIC LCD1602液晶显示器模块实验
#####################################################
import LCD1602    # LCD1602液晶显示屏库
import time
from heartrate_monitor import HeartRateMonitor

# 初始化LCD1602液晶模块
def makerobo_setup():
    LCD1602.makerobo_init(0x27, 1)	# 初始化(设备地址, 背光设置)
    LCD1602.makerobo_write(0, 0, 'sensor starting')     # 显示第一行信息
    LCD1602.makerobo_write(0, 1, 'made by Billy') # 显示第二行信息
    time.sleep(2)                       # 延时2S

bpm1=HeartRateMonitor()
bpm1.getbpm()
bpm1=str(bpm1)
spo21=HeartRateMonitor()
spo21.getspo2()
spo21=str(spo21)
# 循环函数
class Lcd1602(spo21,bpm1):
    def __init__(bpm1,spo21):
        self.bpm=bpm1
        self.spo2=spo21
    def loop(self):
        makerobo_space = 'Heartrate'  # 空显信息
        makerobo_greetings = self.bpm # 显示提示信息
        makerobo_greetings = makerobo_space + str(makerobo_greetings) # 显示信息拼接
        LCD1602.makerobo_write(0, 0, makerobo_greetings)     # 显示第一行信息
        LCD1602.makerobo_write(0, 1, 'lazybone')
    
        textspo2=spo21
        LCD1602.makerobo_write(0, 0, makerobo_greetings)     # 显示第一行信息
        LCD1602.makerobo_write(0, 1,textspo2 ) 
    # 无线循环

# 释放资源
    def destroy():
        pass

# 程序入口
    if __name__ == "__main__":
        try:
            makerobo_setup()      # 初始化信息
            loop(HeartRateMonitor)
        except KeyboardInterrupt: # 当按下Ctrl+C时，将执行destroy()子程序。
            destroy()             # 释放资源