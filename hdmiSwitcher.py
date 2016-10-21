# -*- coding: utf-8 -*-
'''
Created on 2016. 10. 20.

@author: jee1lee
'''

import RPi.GPIO as GPIO


class HdmiSwitcher:

    CHANNEL = 17  # 적외선 송신기 연결 PIN번호
    FREQUENCY = {1: '0000000001fe40bf',  # 리모컨의 각 번호에 맞는 버튼의 frequency 를 설정한다.
                 2: '0000000001fe20df',
                 3: '0000000001fe609f'}

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)    # GPIO 로 시작하는 번호가 아니라, 보드자체의 핀번호를 사용한다.
        GPIO.setup(self.CHANNEL, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def switch(self, buttonNo):
        print(buttonNo, self.FREQUENCY[buttonNo])
        p = GPIO.PWM(self.CHANNEL, self.FREQUENCY[buttonNo])
        p.start(100)    # 최대 출력으로 송신 시
        time.sleep(1)
        p.stop()


if __name__ == "__main__":
    hdmi = HdmiSwitcher()
    hdmi.switch(1)
