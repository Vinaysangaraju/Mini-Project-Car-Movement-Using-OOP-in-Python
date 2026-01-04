class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print("Vehicle is moving at", self.speed, "km/h")


class Engine:
    def start(self):
        print("Engine Has Started")


class Car(Vehicle):
    def __init__(self, brand, speed):
        self.brand = brand
        super().__init__(speed)
        self.engine = Engine()

    def move(self):
        self.engine.start()
        print(self.brand, "Car is moving at", self.speed, "Km/h")

 
    a = Car("Toyota", 220)
    a.move()
