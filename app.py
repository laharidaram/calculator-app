import tkinter as tk
from tkinter import messagebox, ttk
import math
import matplotlib.pyplot as plt
import numpy as np

def evaluate_expression(expression):
    try:
       
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('csc', '1/math.sin')
        expression = expression.replace('sec', '1/math.cos')
        expression = expression.replace('cot', '1/math.tan')
        expression = expression.replace('sqrt', 'math.sqrt')
        expression = expression.replace('log', 'math.log')
        expression = expression.replace('exp', 'math.exp')

        
        result = eval(expression)
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {str(e)}")
        return None
def append_to_expression(value):
    current_text = entry_value.get()

    if value in ")}]":
        if current_text and current_text[-1] in "({[+*/%^-":
            return  
    elif value in "({[":
        
        pass
    entry_value.insert(tk.END, value)
    
def calculate():
    expression = entry_value.get()
    result = evaluate_expression(expression)
    if result is not None:
        result_var.set(f"{result:.5f}")
        history.append(f"{expression} = {result:.5f}")

def plot_graph(operation):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    
    try:
        if operation == "sin":
            y = np.sin(x)
        elif operation == "cos":
            y = np.cos(x)
        elif operation == "tan":
            y = np.tan(x)
        elif operation == "csc":
            y = 1 / np.sin(x)
        elif operation == "sec":
            y = 1 / np.cos(x)
        elif operation == "cot":
            y = 1 / np.tan(x)
        elif operation == "exp":
            y = np.exp(x)
        elif operation == "log":
           
            x = x[x > 0]  
            y = np.log(x)

        plt.figure(figsize=(10, 5))
        plt.plot(x, y, label=f"{operation}(x)")
        plt.ylim(-10, 10)
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.axvline(0, color='black', lw=0.5, ls='--')
        plt.title(f"Graph of {operation}(x)")
        plt.xlabel("x (radians)" if operation in ["sin", "cos", "tan", "csc", "sec", "cot"] else "x")
        plt.ylabel(f"{operation}(x)")
        plt.grid()
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))



def clear_expression():
    entry_value.delete(0, tk.END)

def backspace_expression():
    current_text = entry_value.get()
    entry_value.delete(len(current_text)-1, tk.END)

def toggle_arithmetic():
    trig_frame.grid_remove()
    log_exp_frame.grid_remove()
    graph_frame.grid_remove()
    bracket_frame.grid_remove()
    arithmetic_frame.grid() if not arithmetic_frame.winfo_ismapped() else arithmetic_frame.grid_remove()

def toggle_trigonometry():
    arithmetic_frame.grid_remove()
    log_exp_frame.grid_remove()
    graph_frame.grid_remove()
    bracket_frame.grid_remove()
    trig_frame.grid() if not trig_frame.winfo_ismapped() else trig_frame.grid_remove()

def toggle_log_exp():
    arithmetic_frame.grid_remove()
    trig_frame.grid_remove()
    graph_frame.grid_remove()
    bracket_frame.grid_remove()
    log_exp_frame.grid() if not log_exp_frame.winfo_ismapped() else log_exp_frame.grid_remove()

def toggle_graphs():
    arithmetic_frame.grid_remove()
    trig_frame.grid_remove()
    log_exp_frame.grid_remove()
    bracket_frame.grid_remove()
    graph_frame.grid() if not graph_frame.winfo_ismapped() else graph_frame.grid_remove()

def toggle_brackets():
    arithmetic_frame.grid_remove()
    trig_frame.grid_remove()
    log_exp_frame.grid_remove()
    graph_frame.grid_remove()
    bracket_frame.grid() if not bracket_frame.winfo_ismapped() else bracket_frame.grid_remove()

def unit_conversion():
    def perform_conversion():
        try:
            value = float(value_entry.get())
            from_unit = from_unit_combo.get()
            to_unit = to_unit_combo.get()

            conversion_dict = {
                ("Meters", "Kilometers"): lambda x: x / 1000,
                ("Kilometers", "Meters"): lambda x: x * 1000,
                ("Meters", "Centimeters"): lambda x: x * 100,
                ("Centimeters", "Meters"): lambda x: x / 100,
                ("Kilograms", "Grams"): lambda x: x * 1000,
                ("Grams", "Kilograms"): lambda x: x / 1000,
                ("Inches", "Yards"): lambda x: x / 36,
                ("Yards", "Inches"): lambda x: x * 36,
                ("Litres", "Milliliters"): lambda x: x * 1000,
                ("Milliliters", "Litres"): lambda x: x / 1000,
                ("Km/hr", "M/s"): lambda x: x / 3.6,
                ("M/s", "Km/hr"): lambda x: x * 3.6,
                ("Degrees", "Radians"): lambda x: math.radians(x),
                ("Radians", "Degrees"): lambda x: math.degrees(x),
                ("Miles", "Kilometers"): lambda x: x * 1.60934,
                ("Kilometers", "Miles"): lambda x: x / 1.60934,
                ("Pounds", "Kilograms"): lambda x: x * 0.453592,
                ("Kilograms", "Pounds"): lambda x: x / 0.453592,
                ("Feet", "Meters"): lambda x: x * 0.3048,
                ("Meters", "Feet"): lambda x: x / 0.3048,
                ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
                ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
            }

            if (from_unit, to_unit) in conversion_dict:
                converted_value = conversion_dict[(from_unit, to_unit)](value)
                messagebox.showinfo("Conversion Result", f"{value} {from_unit} = {converted_value:.5f} {to_unit}")
            else:
                messagebox.showerror("Invalid Conversion", "Selected units are not compatible.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    conversion_window = tk.Toplevel(root)
    conversion_window.title("Unit Conversion")
    conversion_window.geometry("400x400")

    tk.Label(conversion_window, text="Value:").grid(row=0, column=0, padx=10, pady=10)
    value_entry = tk.Entry(conversion_window)
    value_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(conversion_window, text="From Unit:").grid(row=1, column=0, padx=10, pady=10)
    from_unit_combo = ttk.Combobox(
        conversion_window,
        values=["Meters", "Kilometers", "Centimeters", "Kilograms", "Grams", "Inches", "Yards", 
                "Litres", "Milliliters", "Km/hr", "M/s", "Degrees", "Radians", "Miles", "Pounds", 
                "Feet", "Celsius", "Fahrenheit"]
    )
    from_unit_combo.set("Meters")
    from_unit_combo.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(conversion_window, text="To Unit:").grid(row=2, column=0, padx=10, pady=10)
    to_unit_combo = ttk.Combobox(
        conversion_window,
        values=["Meters", "Kilometers", "Centimeters", "Kilograms", "Grams", "Inches", "Yards", 
                "Litres", "Milliliters", "Km/hr", "M/s", "Degrees", "Radians", "Miles", "Pounds", 
                "Feet", "Celsius", "Fahrenheit"]
    )
    to_unit_combo.set("Kilometers")
    to_unit_combo.grid(row=2, column=1, padx=10, pady=10)

    convert_button = ttk.Button(conversion_window, text="Convert", command=perform_conversion)
    convert_button.grid(row=3, column=0, columnspan=2, pady=20)


def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("History")
    history_window.geometry("400x300")

    history_text = tk.Text(history_window, height=15, width=50)
    history_text.pack(padx=10, pady=10)
    
    for entry in history:
        history_text.insert(tk.END, entry + "\n")
    history_text.config(state=tk.DISABLED)

# Tkinter UI setup
root = tk.Tk()
root.title("Modern Scientific Calculator")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", background="#8bc34a", foreground="black", borderwidth=0)
style.configure("TLabel", background="#f0f0f0", foreground="black", font=("Arial", 14))

# Input field for expression
tk.Label(root, text="Enter Expression:", font=("Arial", 16), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=(10, 5), sticky="w")
entry_value = tk.Entry(root, width=30, font=("Arial", 14), borderwidth=0, bg="#ffffff", fg="black")
entry_value.grid(row=1, column=0, padx=5, pady=5)

# Result field
tk.Label(root, text="Result:", font=("Arial", 16), bg="#f0f0f0").grid(row=0, column=1, padx=5, pady=(10, 5), sticky="w")
result_var = tk.StringVar()
result_display = tk.Entry(root, textvariable=result_var, font=("Arial", 14), width=20, state='readonly', bg="#e0e0e0", fg="black", borderwidth=0)
result_display.grid(row=1, column=1, padx=5, pady=5)

# History list
history = []

number_frame = tk.Frame(root, bg="#f0f0f0")
number_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Clear', '0', '⌫']
for i, button in enumerate(buttons):
    if button == 'Clear':
        command = clear_expression
    elif button == '⌫':
        command = backspace_expression
    else:
        command = lambda value=button: append_to_expression(value)

    button_widget = ttk.Button(number_frame, text=button, command=command)
    button_widget.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="ew")

# Frame for arithmetic operations
arithmetic_frame = tk.Frame(root, bg="#f0f0f0")
operations = ["+", "-", "*", "/", "%"]
for i, op in enumerate(operations):
    button = ttk.Button(arithmetic_frame, text=op, command=lambda op=op: append_to_expression(f' {op} '))
    button.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

# Frame for trigonometric functions
trig_frame = tk.Frame(root, bg="#f0f0f0")
trig_functions = ["sin", "cos", "tan", "csc", "sec", "cot"]
for i, func in enumerate(trig_functions):
    button = ttk.Button(trig_frame, text=func, command=lambda func=func: append_to_expression(f"{func}("))
    button.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

# Frame for brackets
bracket_frame = tk.Frame(root, bg="#f0f0f0")
brackets = ["(", ")", "{", "}", "[", "]"]
for i, bracket in enumerate(brackets):
    button = ttk.Button(bracket_frame, text=bracket, command=lambda bracket=bracket: append_to_expression(bracket))
    button.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

# Frame for logarithmic and exponential functions
log_exp_frame = tk.Frame(root, bg="#f0f0f0")
log_exp_operations = ["log", "exp"]
for i, op in enumerate(log_exp_operations):
    button = ttk.Button(log_exp_frame, text=op, command=lambda op=op: append_to_expression(f"{op}("))
    button.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

# Frame for plotting options
graph_frame = tk.Frame(root, bg="#f0f0f0")
graph_operations = ["sin", "cos", "tan", "csc", "sec", "cot", "exp", "log"]
for i, func in enumerate(graph_operations):
    button = ttk.Button(graph_frame, text=func, command=lambda func=func: plot_graph(func))
    button.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

# Toggle buttons for frames
toggle_frame = tk.Frame(root, bg="#f0f0f0")
toggle_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
ttk.Button(toggle_frame, text="Arithmetic", command=toggle_arithmetic).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
ttk.Button(toggle_frame, text="Trigonometry", command=toggle_trigonometry).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
ttk.Button(toggle_frame, text="Log/Exp", command=toggle_log_exp).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
ttk.Button(toggle_frame, text="Plot Graphs", command=toggle_graphs).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
ttk.Button(toggle_frame, text="Brackets", command=toggle_brackets).grid(row=0, column=4, padx=5, pady=5, sticky="ew")

# Unit conversion button
ttk.Button(root, text="Unit Conversion", command=unit_conversion).grid(row=4, column=2, padx=10, pady=10, sticky="ew")

# History button
ttk.Button(root, text="History", command=show_history).grid(row=4, column=3, padx=10, pady=10, sticky="ew")

# Equals button for calculation
ttk.Button(root, text="=", command=calculate, style="TButton").grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

root.mainloop()
