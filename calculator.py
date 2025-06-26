import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x568")
        self.root.configure(bg='#f2f2f2')
        
        # Calculator state
        self.current = ""
        self.first_operand = None
        self.operation = None
        
        # Display
        self.display = tk.Label(
            root,
            text="0",
            anchor="e",
            font=("Helvetica", 40),
            bg='#f2f2f2',
            fg='#000000'
        )
        self.display.pack(pady=20, padx=20, fill='x')
        
        # Button frame
        self.button_frame = tk.Frame(root, bg='#f2f2f2')
        self.button_frame.pack(padx=20, pady=10, fill='x')
        
        # Create buttons
        buttons = [
            ('AC', 'C', '%', '÷'),
            ('7', '8', '9', '×'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', '±', '=')
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, text in enumerate(row):
                btn = tk.Button(
                    self.button_frame,
                    text=text,
                    font=("Helvetica", 20),
                    width=3,
                    height=1,
                    bg='#e6e6e6' if text in ['AC', 'C', '%', '÷', '×', '-', '+', '±', '='] else '#ffffff',
                    fg='#000000' if text not in ['AC', 'C'] else '#ff0000',
                    relief='flat',
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky='nsew')
                
        # Configure grid weights
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)
        
    def on_button_click(self, text):
        if text == 'AC':
            self.current = ""
            self.first_operand = None
            self.operation = None
        elif text == 'C':
            self.current = self.current[:-1] if self.current else ""
        elif text in ['+', '-', '×', '÷']:
            if self.current:
                self.first_operand = float(self.current)
                self.operation = text
                self.current = ""
        elif text == '=':
            if self.first_operand is not None and self.operation and self.current:
                second_operand = float(self.current)
                if self.operation == '+':
                    result = self.first_operand + second_operand
                elif self.operation == '-':
                    result = self.first_operand - second_operand
                elif self.operation == '×':
                    result = self.first_operand * second_operand
                elif self.operation == '÷':
                    result = self.first_operand / second_operand
                
                self.current = str(result)
                self.first_operand = None
                self.operation = None
        elif text == '±':
            if self.current:
                self.current = str(float(self.current) * -1)
        elif text == '%':
            if self.current:
                self.current = str(float(self.current) / 100)
        else:
            self.current += text
        
        # Update display
        display_text = self.current if self.current else "0"
        self.display.config(text=display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
