import tkinter as tk
import random
import json


with open("windowTitles.json", "r") as file:
    data = json.load(file)

jsonData = data["windowTitles"]
random_title = random.choice(jsonData)

window = tk.Tk()
window.title(random_title)
window.geometry("450x600")

input1 = tk.StringVar()
input2 = tk.StringVar()

result_label = tk.Label(window, text="Result", font=("Arial", 24))
result_label.pack()

def formatResult(value):
    if value.is_integer():
        return int(value)
    else:
        return f"{value:.1f}"

def calculate(type):
    try:
        num1 = float(input1.get())
        num2 = float(input2.get())
        if type == "add":
            result = num1 + num2
        elif type == "subtract":
            result = num1 - num2
        elif type == "multiply":
            result = num1 * num2
        elif type == "divide":
            if num2 == 0:
                result_label.config(text="Cannot divide by zero!")
                return
            result = num1 / num2
        elif type == "power":
            result = num1 ** num2
        elif type == "average":
            result = (num1 + num2) / 2
        elif type == "max":
            result = max(num1, num2)
        elif type == "min":
            result = min(num1, num2)
        elif type == "abs_diff":
            result = abs(num1 - num2)
        else:
            result_label.config(text="Please enter valid numbers :)")
            return
                 
        result_label.config(text=f"Result: {formatResult(result)}")
    except ValueError:
        result_label.config(text="Please enter valid numbers :)")
    

input1_label = tk.Label(window, text="Enter First Number", font=("Arial", 16))
input1_label.pack(pady=5)
input1_entry = tk.Entry(window, textvariable=input1, font=("Arial", 16))
input1_entry.pack(pady=5)

input2_label = tk.Label(window, text="Enter Second Number", font=("Arial", 16))
input2_label.pack(pady=5)
input2_entry = tk.Entry(window, textvariable=input2, font=("Arial", 16))
input2_entry.pack(pady=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

button_frame2 = tk.Frame(window)
button_frame2.pack(pady=20)

# Knapp for pluss
add_button = tk.Button(button_frame, text="+", font=("Arial", 16), command=lambda: calculate("add"))
add_button.pack(side=tk.LEFT, padx=10, pady=10)

# Knapp for minus
subtract_button = tk.Button(button_frame, text="-", font=("Arial", 16), command=lambda: calculate("subtract"))
subtract_button.pack(side=tk.LEFT, padx=10, pady=10)

# Knapp for ganging
multiply_button = tk.Button(button_frame, text="*", font=("Arial", 16), command=lambda: calculate("multiply"))
multiply_button.pack(side=tk.LEFT, padx=10, pady=10)

# Knapp for deling
divide_button = tk.Button(button_frame, text="/", font=("Arial", 16), command=lambda: calculate("divide"))
divide_button.pack(side=tk.LEFT, padx=10, pady=10)

# Knapp for power
power_button = tk.Button(button_frame, text="^", font=("Arial", 16), command=lambda: calculate("power"))
power_button.pack(side=tk.LEFT, padx=10, pady=10)

# Knapp for max
max_button = tk.Button(button_frame2, text="max", font=("Arial", 16), command=lambda: calculate("max"))
max_button.pack(side=tk.LEFT, padx=10, pady=10)

# Knapp for min
min_button = tk.Button(button_frame2, text="min", font=("Arial", 16), command=lambda: calculate("min"))
min_button.pack(side=tk.LEFT, padx=10, pady=10)

# Knapp for gjennomsnitt
average_button = tk.Button(button_frame2, text="avg", font=("Arial", 16), command=lambda: calculate("average"))
average_button.pack(side=tk.LEFT, padx=10, pady=10)

# Knapp for abs
abs_diff_button = tk.Button(button_frame2, text="diff", font=("Arial", 16), command=lambda: calculate("abs_diff"))
abs_diff_button.pack(side=tk.LEFT, padx=10, pady=10)

window.mainloop()