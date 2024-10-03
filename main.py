from TrafficLight import TrafficLight
from Junction import Junction
import time
import random

#main program
lightOne = TrafficLight(1)
lightTwo = TrafficLight(2)
lightOne.set_light_colour("green")
junction = Junction(lightOne, lightTwo)

while True: 
    #initial state of traffic
    print(f"{junction}")

    #if the red light has traffic, it'll switch the traffic lights
    redLight = junction.check_red_light()
    if redLight.get_traffic():
        print(f"\nTRAFFIC DETECTED AT {redLight}:\n{junction}")
        junction.toggle(redLight)
    else:
        time.sleep(3)

    #attempt at spawning traffic at the red light
    junction.update_traffic()

    
    print("END============================================END\n")

