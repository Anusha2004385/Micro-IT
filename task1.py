import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field for input and result
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create buttons dynamically
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == '=':
            tk.Button(root, text=btn_text, width=5, height=2, font=('Arial', 18),
                      command=calculate).grid(row=i+1, column=j)
        else:
            tk.Button(root, text=btn_text, width=5, height=2, font=('Arial', 18),
                      command=lambda val=btn_text: button_click(val)).grid(row=i+1, column=j)

# Clear button
tk.Button(root, text='C', width=22, height=2, font=('Arial', 18), command=clear).grid(row=5, column=0, columnspan=4)

# Run the application
root.mainloop()
