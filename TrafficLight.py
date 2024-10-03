class TrafficLight:
    def __init__(self, number: int, light_colour="red", traffic=False):
        self.number = number
        self.light_colour = light_colour
        self.traffic = traffic
    
    def get_light_colour(self) -> str:
        return self.light_colour

    def set_light_colour(self, light_colour: str):
        self.light_colour = light_colour
    
    def get_traffic(self) -> bool:
        return self.traffic
    
    def set_traffic(self, traffic: bool):
        self.traffic = traffic

    def __str__(self):
        return f"light {str(self.number)}"
    