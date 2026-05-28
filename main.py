# main.py
# This file runs a simple calculator GUI using Python's Tkinter library.

import tkinter as tk  # Import Tkinter and alias it as tk for convenience.


class CalculatorApp(tk.Tk):  # Create a GUI application class that inherits from Tk.
    def __init__(self):  # Initialize the app when the class is instantiated.
        super().__init__()  # Call the parent constructor to initialize the Tk root.
        self.title("Calculator")  # Set the window title.
        self.resizable(False, False)  # Prevent the window from being resized.

        self.expression = ""  # Store the current expression string entered by the user.

        self.display = tk.Entry(self, font=("Arial", 20), justify="right")  # Create a text input widget as display.
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")  # Place display at top.
        self.display.insert(0, "0")  # Set initial display value.

        self._build_buttons()  # Create and place the calculator buttons.


    def _build_buttons(self):  # Define a helper method to build calculator buttons.
        buttons = [  # Create a list describing all button texts and their grid positions.
            ("C", 1, 0), ("⌫", 1, 1), ("/", 1, 2), ("*", 1, 3),  # Row 1 buttons.
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),  # Row 2 buttons.
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),  # Row 3 buttons.
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),  # Row 4 buttons.
            ("0", 5, 0), (".", 5, 1), ("00", 5, 2), (" ", 5, 3),  # Row 5 buttons (" " is a filler).
        ]  # End of button definitions.

        for (text, r, c) in buttons:  # Iterate over each button definition.
            if text == " ":  # Check if this is the filler cell.
                continue  # Skip creating a button for the filler cell.

            width = 5  # Define a uniform button width.
            btn = tk.Button(self, text=text, font=("Arial", 18), width=width, height=2)  # Create a Tk button.
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")  # Place the button in the grid.

            if text in "0123456789":  # If button is a digit.
                btn.configure(command=lambda t=text: self._append_digit(t))  # Append that digit to expression.
            elif text == ".":  # If button is decimal point.
                btn.configure(command=lambda t=text: self._append_decimal(t))  # Append decimal to expression.
            elif text in "+-*/":  # If button is an operator.
                btn.configure(command=lambda t=text: self._append_operator(t))  # Append operator to expression.
            elif text == "C":  # If clear button.
                btn.configure(command=self._clear)  # Clear expression and reset display.
            elif text == "⌫":  # If backspace button.
                btn.configure(command=self._backspace)  # Remove last character.
            elif text == "=":  # If equals button.
                btn.configure(command=self._calculate)  # Evaluate expression.

            # Note: other texts are skipped above.

        # Configure grid weights for consistent resizing within fixed-size window.
        for i in range(6):  # Set row weights for 6 rows (0 to 5).
            self.grid_rowconfigure(i, weight=1)  # Give equal weight to rows.
        for j in range(4):  # Set column weights for 4 columns (0 to 3).
            self.grid_columnconfigure(j, weight=1)  # Give equal weight to columns.


    def _append_digit(self, digit):  # Append a digit (0-9) to the expression.
        self.expression += digit  # Add the digit to the expression string.
        self.display.delete(0, tk.END)  # Clear the current display content.
        self.display.insert(0, self.expression)  # Show updated expression.


    def _append_decimal(self, dot):  # Append a decimal point to the expression safely.
        if not self.expression:  # If expression is empty, start with "0.".
            self.expression = "0."  # Initialize expression to include decimal.
        else:  # Otherwise, check if the current number already has a decimal.
            last_number = self._get_last_number()  # Get the substring of the last number.
            if "." not in last_number:  # If the last number doesn't contain a decimal.
                self.expression += dot  # Append the decimal point.
        self.display.delete(0, tk.END)  # Clear the display.
        self.display.insert(0, self.expression if self.expression else "0")  # Update display.


    def _append_operator(self, op):  # Append an operator to the expression.
        if not self.expression:  # If expression is empty, allow leading negative/starting operators? We'll block.
            return  # Do nothing to avoid invalid expression starting with operator.

        if self.expression[-1] in "+-*/":  # If last character is already an operator.
            self.expression = self.expression[:-1] + op  # Replace operator with new operator.
        else:  # Otherwise append operator.
            self.expression += op  # Add operator.

        self.display.delete(0, tk.END)  # Clear display.
        self.display.insert(0, self.expression)  # Update display with expression.


    def _get_last_number(self):  # Extract the last number segment from the expression.
        operators = "+-*/"  # Define operator characters.
        idx = -1  # Default index meaning "not found".
        for ch in operators:  # Iterate through each operator.
            pos = self.expression.rfind(ch)  # Find the last position of that operator.
            if pos > idx:  # Track the rightmost operator position.
                idx = pos  # Update the rightmost index.
        if idx == -1:  # If there is no operator in expression.
            return self.expression  # Return whole expression as last number.
        return self.expression[idx + 1 :]  # Return substring after the last operator.


    def _clear(self):  # Clear button logic.
        self.expression = ""  # Reset expression to empty.
        self.display.delete(0, tk.END)  # Clear the display.
        self.display.insert(0, "0")  # Reset display to 0.


    def _backspace(self):  # Backspace button logic.
        if not self.expression:  # If expression is empty, do nothing.
            return  # Exit early.
        self.expression = self.expression[:-1]  # Remove last character from expression.
        self.display.delete(0, tk.END)  # Clear display.
        self.display.insert(0, self.expression if self.expression else "0")  # Update display.


    def _calculate(self):  # Evaluate button logic.
        if not self.expression:  # If expression is empty.
            return  # Do nothing.

        # Replace any trailing operator with nothing to avoid syntax errors.
        while self.expression and self.expression[-1] in "+-*/":  # While the expression ends with operator.
            self.expression = self.expression[:-1]  # Remove trailing operator(s).

        if not self.expression:  # If expression became empty after cleanup.
            self.display.delete(0, tk.END)  # Clear display.
            self.display.insert(0, "0")  # Show 0.
            return  # Exit.

        try:  # Use try/except to handle invalid expressions.
            result = eval(self.expression)  # Evaluate expression (only operators and numbers are expected).
            # Format result to remove unnecessary trailing .0 when it's an integer.
            if isinstance(result, float) and result.is_integer():  # Check if float result is an integer.
                result = int(result)  # Convert to int for cleaner display.

            self.expression = str(result)  # Set expression to the result for further calculations.
            self.display.delete(0, tk.END)  # Clear display.
            self.display.insert(0, self.expression)  # Show result.
        except Exception:  # Catch any errors (like division by zero or syntax errors).
            self.display.delete(0, tk.END)  # Clear display.
            self.display.insert(0, "Error")  # Show error message.
            self.expression = ""  # Reset expression to avoid repeated errors.


if __name__ == "__main__":  # This block runs only when you execute the script directly.
    app = CalculatorApp()  # Create the calculator application.
    app.mainloop()  # Start the Tkinter event loop.

