class Calculator:
    def __init__(self):
        print("Calculator initialized. Ready for operations.")

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Cannot divide by zero!"
        return x / y

    def power(self, x, y):
        return x ** y

if __name__ == "__main__":
    my_calculator = Calculator()

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Exit")

        choice = input("Enter choice(1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {my_calculator.add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {my_calculator.subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {my_calculator.multiply(num1, num2)}")
            elif choice == '4':
                result = my_calculator.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                print(f"{num1} ** {num2} = {my_calculator.power(num1, num2)}")
        elif choice == '6':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")