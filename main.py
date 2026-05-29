# Import tkinter library
import tkinter as tk


# =========================
# CREATE MAIN WINDOW
# =========================

# Create the main application window
root = tk.Tk()

# Set window title
root.title("Simple Calculator")

# Set window size
# Format = "width x height"
root.geometry("300x400")


# =========================
# INPUT / DISPLAY SCREEN
# =========================

# Create input field where numbers and results appear
entry = tk.Entry(
    root,                  # Parent window
    width=20,              # Width of input box
    font=("Arial", 20),    # Font style and size
    borderwidth=5          # Border thickness
)

# Place entry field using grid
# columnspan=4 means it covers 4 columns
entry.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=10
)


# =========================
# FUNCTION: BUTTON CLICK
# =========================

# This function runs when number/operator button clicked
def click(number):

    # Get current text from display
    current = entry.get()

    # Clear current text
    entry.delete(0, tk.END)

    # Add new number/operator to existing text
    entry.insert(0, str(current) + str(number))


# =========================
# FUNCTION: CLEAR SCREEN
# =========================

# Clears everything from display
def clear():

    # Delete from position 0 to END
    entry.delete(0, tk.END)


# =========================
# FUNCTION: CALCULATE RESULT
# =========================

# Runs when "=" button clicked
def equal():

    # eval() calculates mathematical expression
    # Example: "5+3" becomes 8
    result = eval(entry.get())

    # Clear display
    entry.delete(0, tk.END)

    # Show result on display
    entry.insert(0, result)


# =========================
# NUMBER BUTTONS
# =========================

# Button 1
button_1 = tk.Button(
    root,
    text="1",              # Button text
    padx=20,               # Horizontal padding
    pady=20,               # Vertical padding

    # lambda passes value to function
    command=lambda: click(1)
)

# Button 2
button_2 = tk.Button(
    root,
    text="2",
    padx=20,
    pady=20,
    command=lambda: click(2)
)

# Button 3
button_3 = tk.Button(
    root,
    text="3",
    padx=20,
    pady=20,
    command=lambda: click(3)
)

# Button 4
button_4 = tk.Button(
    root,
    text="4",
    padx=20,
    pady=20,
    command=lambda: click(4)
)

# Button 5
button_5 = tk.Button(
    root,
    text="5",
    padx=20,
    pady=20,
    command=lambda: click(5)
)

# Button 6
button_6 = tk.Button(
    root,
    text="6",
    padx=20,
    pady=20,
    command=lambda: click(6)
)

# Button 7
button_7 = tk.Button(
    root,
    text="7",
    padx=20,
    pady=20,
    command=lambda: click(7)
)

# Button 8
button_8 = tk.Button(
    root,
    text="8",
    padx=20,
    pady=20,
    command=lambda: click(8)
)

# Button 9
button_9 = tk.Button(
    root,
    text="9",
    padx=20,
    pady=20,
    command=lambda: click(9)
)

# Button 0
button_0 = tk.Button(
    root,
    text="0",
    padx=20,
    pady=20,
    command=lambda: click(0)
)


# =========================
# OPERATOR BUTTONS
# =========================

# Addition button
button_add = tk.Button(
    root,
    text="+",
    padx=20,
    pady=20,
    command=lambda: click("+")
)

# Subtraction button
button_sub = tk.Button(
    root,
    text="-",
    padx=20,
    pady=20,
    command=lambda: click("-")
)

# Multiplication button
button_mul = tk.Button(
    root,
    text="*",
    padx=20,
    pady=20,
    command=lambda: click("*")
)

# Division button
button_div = tk.Button(
    root,
    text="/",
    padx=20,
    pady=20,
    command=lambda: click("/")
)


# =========================
# EQUAL BUTTON
# =========================

# Calculates final result
button_equal = tk.Button(
    root,
    text="=",
    padx=20,
    pady=20,
    command=equal
)


# =========================
# CLEAR BUTTON
# =========================

# Clears calculator screen
button_clear = tk.Button(
    root,
    text="C",
    padx=20,
    pady=20,
    command=clear
)


# =========================
# PLACE BUTTONS USING GRID
# =========================

# First row
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

# Second row
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

# Third row
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

# Fourth row
button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)


# =========================
# RUN APPLICATION
# =========================

# Keeps window open and running
root.mainloop()