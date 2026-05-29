import tkinter as tk

# Create window
root = tk.Tk()

root.title("Simple Calculator")
root.geometry("300x250")


# Function for addition
def add_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    result = num1 + num2

    result_label.config(text="Result: " + str(result))


# First input box
entry1 = tk.Entry(root)
entry1.pack(pady=10)

# Second input box
entry2 = tk.Entry(root)
entry2.pack(pady=10)

# Add button
add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run window
root.mainloop()