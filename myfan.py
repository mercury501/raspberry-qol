#!/usr/bin/env python3

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

pin = 18





def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.setwarnings(False)
	GPIO.setup(15,GPIO.OUT)
	return

def getCPUtemperature():
	temp = os.popen('vcgencmd measure_temp').readline()
	temp = temp.replace("temp=","")
	temp = temp.replace("'C\n","")
	return temp

def fanON():
	setPin(True)
	return

def fanOFF():
	setPin(False)
	return

def getTEMP(p,lastTMP,dc):
	
	return

def setPin(mode):
	GPIO.output(pin,mode)
	return

try:
	dc = 50
	lastTMP = 0

	setup()
	GPIO.output(15,True)
	p = GPIO.PWM(pin,50)
	p.start(0)
	while True:
		CPU_temp = float(getCPUtemperature())
		if CPU_temp >= 70:
			p.ChangeDutyCycle(100)
		if CPU_temp >=65 and CPU_temp < 70:
			p.ChangeDutyCycle(85)
		if CPU_temp > 60 and CPU_temp < 65:
			p.ChangeDutyCycle(70)
		if CPU_temp > 50 and CPU_temp <= 55:
			p.ChangeDutyCycle(45)
		if CPU_temp >55 and CPU_temp <= 60:
			p.ChangeDutyCycle(60)
		if CPU_temp < 50:
			p.ChangeDutyCycle(30)
		print(CPU_temp)
		print("------------------------")
		sleep(5)

except KeyboardInterrupt:
	GPIO.cleanup()
