from TrafficLight import TrafficLight
import time
import random

def checkRedLight(lightOne: TrafficLight, lightTwo: TrafficLight) -> TrafficLight:
    """
    returns the red light
    """
    if lightOne.getLightColour == "red":
        return lightOne
    return lightTwo
 
def updateRedLight():
    redLight = checkRedLight()
    return random.randint(0,1)



#main program
lightOne = TrafficLight()
lightTwo = TrafficLight()
lightOne.setLightColour("green")

for i in range(10):
    redLight = checkRedLight(lightOne, lightTwo)
    