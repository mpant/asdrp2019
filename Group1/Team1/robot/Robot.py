#This code was written by Rishub Shah

import speech_recognition as sr
import time
import random
r=sr.Recognizer()
mic=sr.Microphone()

while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    cmd=r.recognize_google(audio)
    #The print statements are just placeholder code until I can implement the EV3 Code.

    if cmd=='move forward':
        print('Moving Forward')
    elif cmd=='turn right':
        print('Turning Right')
    elif cmd=='turn left':
        print('Turning Left')
    elif cmd=='move backward' or cmd == 'move back':
        print('Moving Backward')
    elif cmd=='stop':
        print('Stopping')
        break