class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_slot = big
        self.big_cnt = 0
        self.medium_slot = medium
        self.medium_cnt = 0
        self.small_slot = small
        self.small_cnt = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_cnt < self.big_slot:
                self.big_cnt += 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium_cnt < self.medium_slot:
                self.medium_cnt += 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small_cnt < self.small_slot:
                self.small_cnt += 1
                return True
            else:
                return False
        
        else:
            raise ImplementationError(f"carType {carType} does not exist")
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)