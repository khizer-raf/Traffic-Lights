from TrafficLight import TrafficLight
import random
import time

class Junction:
    def __init__(self, lightOne: TrafficLight, lightTwo: TrafficLight):
        self.lightOne = lightOne
        self.lightTwo = lightTwo
    
    def check_red_light(self) -> TrafficLight:
        """
        returns the red light
        """
        if self.lightOne.get_light_colour() == "red":
            return self.lightOne
        return self.lightTwo

    def update_traffic(self):
        """
        random chance of spawning traffic on a red light
        """
        redLight = self.check_red_light()
        redLight.set_traffic(bool(random.randint(0,1))) 
    
    def toggle(self, redLight: TrafficLight): 
        """
        sets the given light to green and the other to red
        """
        redLight.set_light_colour("green")
        redLight.set_traffic(False)

        if redLight == self.lightOne:
            self.lightTwo.set_light_colour("red")
        else:  
            self.lightOne.set_light_colour("red")

        #buffer to avoid light instantly switching back and forth during high vol traffic        
        time.sleep(3)

    def __str__(self):
        return f"{self.lightOne} | colour: {self.lightOne.get_light_colour()}, traffic: {self.lightOne.get_traffic()}\n{self.lightTwo} | colour: {self.lightTwo.get_light_colour()}, traffic: {self.lightTwo.get_traffic()}"
