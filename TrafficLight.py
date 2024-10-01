class TrafficLight:
    def __init__(self):
        """
        :light_colour: str value. Set to red by default
        :traffic: int value. 0 if no traffic at the light, 1 if there is
        """
        self.light_colour = "red"
        self.traffic = 0
    
    def getLightColour(self) -> str:
        return self.light_colour

    def setLightColour(self, light_colour: str):
        self.light_colour = light_colour
    
    def getTraffic(self) -> bool:
        return self.traffic
    
    def setTraffic(self, traffic: bool):
        self.traffic = traffic

    