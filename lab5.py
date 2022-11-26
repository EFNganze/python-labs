class Rocket:

    def __init__(self, weight, fuel):
        self.rocket_weight = weight
        self.fuel_weight = fuel
        self.engine_running = (fuel > 0)
    
    def spend_fuel(self, count):
        self.fuel_weight -= count

        if self.fuel_weight > 0:
            return True
        
        self.fuel_weight = 0
        self.engine_running = False
        return False
    
    def get_fuel_level(self):
        return self.fuel_weight
    
    def get_total_weight(self):
        return self.fuel_weight + self.rocket_weight

    def get_is_engine_running(self):
        return self.engine_running
