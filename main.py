import tkinter as tk

window = tk.Tk()
window.title("Terraria > Minecraft")
window.geometry("400x600")

input1 = tk.StringVar()
input2 = tk.StringVar()

result_label = tk.Label(window, text="Result", font=("Arial", 24))
result_label.pack()

def add():
    try:
        num1 = float(input1.get())
        num2 = float(input2.get())
        result = num1 + num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers :)")

def subtract():
    try:
        num1 = float(input1.get())
        num2 = float(input2.get())
        result = num1 - num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers :)")

def multiply():
    try: 
        num1 = float(input1.get())
        num2 = float(input2.get())
        result = num1 * num2
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers :)")

def divide():
    try:
        num1 = float(input1.get())
        num2 = float(input2.get())
        if num2 == 0:
            result_label.config(text="Error: Divison by zero")
        else:
            result = num1 / num2
            result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please ender valdig nummbers :)")
    

input1_label = tk.Label(window, text="Enter First Number", font=("Arial", 16))
input1_label.pack(pady = 5)
input1_entry = tk.Entry(window, textvariable=input1, font=("Arial", 16))
input1_entry.pack(pady = 5)

input2_label = tk.Label(window, text="Enter Second Number", font=("Arial", 16))
input2_label.pack(pady = 5)
input2_entry = tk.Entry(window, textvariable=input2, font=("Arial", 16))
input2_entry.pack(pady = 5)

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

#Knapp for pluss
add_button = tk.Button(button_frame, text="+", font=("Arial", 16), command=add)
add_button.pack(side=tk.LEFT, padx=10, pady=10)

#knapp fo minus
subtract_button = tk.Button(button_frame, text="-", font=("Arial", 16), command=subtract)
subtract_button.pack(side=tk.LEFT, padx=10, pady=10)

#knapp for ganging
multiply_button = tk.Button(button_frame, text="*", font=("Arial", 16), command=multiply)
multiply_button.pack(side=tk.LEFT, padx=10, pady=10)

#knapp for deling
divide_button = tk.Button(button_frame, text="/", font=("Arial", 16), command=divide)
divide_button.pack(side=tk.LEFT, padx=10, pady=10)

window.mainloop()