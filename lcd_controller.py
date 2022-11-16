#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################################

import time
import smbus

makerobo_BUS = smbus.SMBus(1)

# IIC LCD1602 液晶模块写入字
def makerobo_write_word(addr, data):
	global makerobo_BLEN
	makerobo_temp = data
	if makerobo_BLEN == 1:
		makerobo_temp |= 0x08
	else:
		makerobo_temp &= 0xF7
	makerobo_BUS.write_byte(addr ,makerobo_temp) # set the address of IIC LCD1602 liquid crystal module.

# IIC LCD1602 send command
def  makerobo_send_command(comm):
	# Send bit7-4 first
	lcd_buf = comm & 0xF0
	lcd_buf |= 0x04               # RS = 0, RW = 0, EN = 1
	makerobo_write_word(LCD_ADDR ,lcd_buf)
	time.sleep(0.002)
	lcd_buf &= 0xFB               # make EN = 0
	makerobo_write_word(LCD_ADDR ,lcd_buf)

	# Next send bit3-0 bits
	lcd_buf = (comm & 0x0F) << 4
	lcd_buf |= 0x04               # RS = 0, RW = 0, EN = 1
	makerobo_write_word(LCD_ADDR ,lcd_buf)
	time.sleep(0.002)
	lcd_buf &= 0xFB               # make EN = 0
	makerobo_write_word(LCD_ADDR ,lcd_buf)

# IIC LCD1602 send data
def makerobo_send_data(data):
	# Send bit7-4 first
	lcd_buf = data & 0xF0
	lcd_buf |= 0x05               # RS = 1, RW = 0, EN = 1
	makerobo_write_word(LCD_ADDR ,lcd_buf)
	time.sleep(0.002)
	lcd_buf &= 0xFB               # make EN = 0
	makerobo_write_word(LCD_ADDR ,lcd_buf)

	# Next send bit3-0 bits
	lcd_buf = (data & 0x0F) << 4
	lcd_buf |= 0x05               # RS = 1, RW = 0, EN = 1
	makerobo_write_word(LCD_ADDR ,lcd_buf)
	time.sleep(0.002)
	lcd_buf &= 0xFB               # make EN = 0
	makerobo_write_word(LCD_ADDR ,lcd_buf)

# IIC LCD1602 initialization
def  makerobo_init(addr, bl):
	global LCD_ADDR
	global makerobo_BLEN
	LCD_ADDR = addr
	makerobo_BLEN = bl
	try:
		makerobo_send_command(0x33) # must be initialized to 8-wire mode first
		time.sleep(0.005)
		makerobo_send_command(0x32) # then initialize to 4 row mode
		time.sleep(0.005)
		makerobo_send_command(0x28) # 2 rows & 5*7 dots
		time.sleep(0.005)
		makerobo_send_command(0x0C) # enable cursorless display
		time.sleep(0.005)
		makerobo_send_command(0x01) # clear display
		makerobo_BUS.write_byte(LCD_ADDR, 0x08)
	except:
		return False
	else:
		return True

# LCD 1602 clear display function
def makerobo_clear():
	makerobo_send_command(0x01)  # clear display

# LCD 1602 enable backlight display
def makerobo_openlight():  
	makerobo_BUS.write_byte(0x27,0x08)  # enable backlight display command
	makerobo_BUS.close()                # close the bus

# LCD 1602 display function
def makerobo_write(lcd_x, lcd_y, lcd_str):
	# select row and column
	if lcd_x < 0:
		lcd_x = 0
	if lcd_x > 15:
		lcd_x = 15
	if lcd_y <0:
		lcd_y = 0
	if lcd_y > 1:
		lcd_y = 1

	# move cursor
	lcd_addr = 0x80 + 0x40 * lcd_y + lcd_x
	makerobo_send_command(lcd_addr)    # send address

	for chr in lcd_str:                  # get string length
		makerobo_send_data(ord(chr)) # send display

# program entry
if __name__ == '__main__':
	# 15*2

	makerobo_init(0x27, 1)          # initialize the display
	makerobo_write(4, 0, 'HSQ smart')   # display "Hello" on the first line
	makerobo_write(7, 1, 'HSQ YYDS')  # display "world!" on the second line


