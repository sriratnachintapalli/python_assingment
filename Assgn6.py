class Car:
    # Class variable to keep track of the number of cars created
    num_cars = 0

    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        self.running = False
        self.speed = 0
        # Increment the count of cars created
        Car.num_cars += 1

    def start(self):
        if not self.running:
            self.running = True
            return "Car started."
        else:
            return "Car is already running."

    def stop(self):
        if self.running:
            self.running = False
            self.speed = 0
            return "Car stopped."
        else:
            return "Car is not running."

    def accelerate(self, speed_increase):
        if self.running:
            self.speed += speed_increase
            return f"Car accelerated to {self.speed} mph."
        else:
            return "Car is not running. Please start the car first."

    @classmethod
    def get_num_cars(cls):
        return cls.num_cars

# Create some car instances
car1 = Car("Toyota", "Blue", 25000)
car2 = Car("Honda", "Red", 30000)

# Start and accelerate car1
print(car1.start())
print(car1.accelerate(40))

# Stop car2
print(car2.stop())

# Check the number of cars created
num_cars = Car.get_num_cars()
print("Number of Cars Created:", num_cars)
