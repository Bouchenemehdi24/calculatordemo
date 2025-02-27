import tkinter as tk

def click_button(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")

window = tk.Tk()
window.title("Simple Calculator")

display = tk.Entry(window, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == '=':
        tk.Button(window, text=button_text, padx=40, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif button_text == 'C':
        tk.Button(window, text=button_text, padx=40, pady=20, command=clear_display).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button_text, padx=40, pady=20, command=lambda b=button_text: click_button(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()