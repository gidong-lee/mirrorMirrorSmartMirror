# -*- coding: utf-8 -*-
'''
Created on 2016. 10. 20.

@author: jee1lee
'''

import RPi.GPIO as GPIO

CHANNEL = 17 # 적외선 송신기 연결 PIN번호
FREQUENCY = [[1, 0.5],  # 리모컨의 각 번호에 맞는 버튼의 frequency 를 설정한다. 
             [2, 1],
             [3, 1.5]] 

GPIO.setmode(GPIO.BOARD)    # GPIO 로 시작하는 번호가 아니라, 보드자체의 핀번호를 사용한다. 
GPIO.setup(CHANNEL, GPIO.OUT)

def switch(inputNo):
    p = GPIO.PWM(CHANNEL, FREQUENCY[inputNo])
    p.start(100)    # 최대 출력으로 송신 시
    time.sleep(1)
    p.stop()
    GPIO.cleanup()
