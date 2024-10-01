class TrafficLight:
    def __init__(self):
        self.light_colour = "red"
        #self.traffic stores if there are cars waiting at a red light
        self.traffic = False
    
    def getLightColour(self):
        return self.light_colour

    def setLightColour(self, light_colour):
        self.light_colour = light_colour
    
    def getTraffic(self):
        return self.traffic
    
    def setTraffic(self, traffic):
        self.traffic = traffic

    


    
