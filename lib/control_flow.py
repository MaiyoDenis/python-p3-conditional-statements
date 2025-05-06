#!/usr/bin/env python3

def admin_login(username, password):
    # Accept username case insensitively and password "12345"
    valid_username = "admin"
    valid_password = "12345"
    if username.lower() == valid_username and password == valid_password:
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    # Return weather description based on specific temperature ranges
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif 65 <= temperature <= 85:
        return "It's perfect out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's moderate"

def fizzbuzz(num):
    # Classic fizzbuzz implementation with int return for non-multiples
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    # Basic arithmetic operations with symbols and error handling
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
