import math
import tkinter as tk
from tkinter import messagebox

# Console Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Error! Division by zero." if y == 0 else x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative number doesn't exist."
    return math.factorial(x)

# Safe Eval Function
def safe_eval(expression):
    try:
        allowed_chars = "0123456789+-*/().^%"
        if any(char not in allowed_chars for char in expression):
            return "Error: Invalid characters used!"
        return eval(expression.replace("^", "**"))  # Allow power operation
    except Exception as e:
        return f"Error: {e}"

# Console Calculator
def console_calculator():
    while True:
        print("\n📌 Simple Calculator")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Modulus (%)")
        print("6. Power (x^y)")
        print("7. Square Root (√x)")
        print("8. Factorial (x!)")
        print("9. Eval-Based Calculator")
        print("10. Exit")

        choice = input("Select an operation (1-10): ")

        if choice == '10':
            print("Exiting... Thank you!")
            break  # Exit the loop

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
                elif choice == '6':
                    print(f"Result: {num1}^{num2} = {power(num1, num2)}")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice in ('7', '8'):
            try:
                num = int(input("Enter a number: "))

                if choice == '7':
                    print(f"Result: √{num} = {square_root(num)}")
                elif choice == '8':
                    print(f"Result: {num}! = {factorial(num)}")

            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == '9':
            expr = input("Enter a mathematical expression: ")
            print("Result:", safe_eval(expr))
        
        else:
            print("Invalid choice! Please select a valid operation.")

# GUI Calculator Functions
def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# GUI Calculator
def gui_calculator():
    global entry
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x400")

    entry = tk.Entry(root, width=20, font=("Arial", 20), bd=8, relief="ridge", justify="right")
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("C", "0", "=", "+"),
    ]

    for row_idx, row in enumerate(buttons, start=1):
        for col_idx, button_text in enumerate(row):
            button = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 15),
                               command=lambda bt=button_text: on_click(bt))
            button.grid(row=row_idx, column=col_idx)

    root.mainloop()

# Main Program
if __name__ == "__main__":
    print("🔥 Welcome to the Ultimate Calculator! 🔥")
    print("1. Console-Based Calculator")
    print("2. GUI-Based Calculator")
    choice = input("Choose mode (1 or 2): ")

    if choice == "1":
        console_calculator()
    elif choice == "2":
        gui_calculator()
    else:
        print("Invalid choice! Exiting...")
