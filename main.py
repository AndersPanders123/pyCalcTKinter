import tkinter as tk

window = tk.Tk()
window.title("Terraria > Minecraft")
window.geometry("400x600")

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

window.mainloop()
