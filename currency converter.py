import tkinter as tk
from tkinter import ttk
import requests

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        
        # Get exchange rates (optional: replace with hardcoded rates if needed)
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        
        if to_currency in data['rates']:
            rate = data['rates'][to_currency]
            result = amount * rate
            label_result.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            label_result.config(text="Currency not found!")
    except Exception as e:
        label_result.config(text=f"Error: {e}")

# Create main application window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")

# Input fields and labels
label_amount = tk.Label(root, text="Amount:")
label_amount.pack(pady=5)

entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

label_from = tk.Label(root, text="From Currency:")
label_from.pack(pady=5)

combo_from = ttk.Combobox(root, values=["USD", "EUR", "INR", "GBP", "AUD", "CAD"])
combo_from.pack(pady=5)
combo_from.set("USD")

label_to = tk.Label(root, text="To Currency:")
label_to.pack(pady=5)

combo_to = ttk.Combobox(root, values=["USD", "EUR", "INR", "GBP", "AUD", "CAD"])
combo_to.pack(pady=5)
combo_to.set("EUR")

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_currency)
button_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=20)

# Start the GUI loop
root.mainloop()
