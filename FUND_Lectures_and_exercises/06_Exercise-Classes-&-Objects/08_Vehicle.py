class Vehicle:

    def __init__(self, vehicle_type, model, price):
        self.vehicle_type = vehicle_type
        self.model = model
        self.price = price
        self.owner_car = None

    def buy(self, money: int, owner: str):
        if self.owner_car is None:
            return "Car already sold"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            self.owner_car = owner
            change = money - self.price
            return f"Successfully bought a {self.vehicle_type}. Change: {change}"

    def sell(self):
        if self.owner_car is not None:
            self.owner_car = None
            return True
        else:
            return "Vehicle has no owner"

    