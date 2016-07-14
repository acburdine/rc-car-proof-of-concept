#!/usr/bin/python

from legopi.lib import xbox_read
import piplates.MOTORplate as motor

motor_addr = 0
dc_addr = 1
def_speed = 100.0
def_accel = 0.0
dir = None
motor_dir1 = None
motor_dir2 = None
previousX = 0
xStopped = False
previousY = 0
yDir = None

for event in xbox_read.event_stream(deadzone=12000):
    if event.key == 'X1':
    if (previousX != 0 and (event.value == 0 or (previousX<0) == (event.value<0))):
            motor.dcSTOP(motor_addr, dc_addr)
            xStopped = True

        previousX = event.value

        if event.value < 0:
        dir = 'ccw'
        elif event.value > 0:
            dir = 'cw'

        if (event.value != 0 and xStopped):
            xStopped = False
            motor.dcCONFIG(motor_addr, dc_addr, dir, def_speed, def_accel)
            motor.dcSTART(motor_addr, dc_addr)
    elif event.key == 'Y1':
        ySpeed = event.value / 327.7
        motor.dcSTOP(motor_addr, 3)
        if event.value < 0:
            yDir = 'cw'
            ySpeed *= -1
        elif event.value > 0:
            yDir = 'ccw'

    if event.value != 0:
            motor.dcCONFIG(motor_addr, 3, yDir, ySpeed, 0)
            motor.dcSTART(motor_addr, 3)

