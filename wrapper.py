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
Hrcalc=importlib.import_module('hrcalc')
Max30102=importlib.import_module('max30102')
#INIT FUCTIONS

# now initialize all libarary for starting up
#set up fundamental variables to judge crtical situations

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

def makerobo_destroy():
    heartrate_monitor.stop_sensor()

if __name__ == "__main__":
    try:
        makerobo_setup()
        makerobo_loop()
    except KeyboardInterrupt:
        makerobo_destory()
