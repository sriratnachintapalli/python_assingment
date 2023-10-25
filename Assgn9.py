class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num

    def substract(self, num):
        self.value -= num

    def multiply(self, num):
        self.value *= num

    def divide(self, num):
        if num == 0:
            return "Cannot divide by zero."
        self.value /= num

    # Operator overloading methods
    def __add__(self, num):
        result = self.value + num
        return Calculator(result)

    def __sub__(self, num):
        result = self.value - num
        return Calculator(result)

    def __mul__(self, num):
        result = self.value * num
        return Calculator(result)

    def __truediv__(self, num):
        if num == 0:
            return "Cannot divide by zero."
        result = self.value / num
        return Calculator(result)

    def __str__(self):
        return str(self.value)

# Create a Calculator instance
calc = Calculator(10)

# Using methods for basic arithmetic operations
calc.add(5)
calc.substract(3)
calc.multiply(2)
calc.divide(4)

print("Result using methods:", calc)

# Using operator overloading
calc1 = calc + 5
calc2 = calc1 - 3
calc3 = calc2 * 2
calc4 = calc3 / 4

print("Result using operator overloading:", calc4)

