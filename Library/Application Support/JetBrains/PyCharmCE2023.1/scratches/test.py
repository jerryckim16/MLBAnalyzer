import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch the BTC price
def get_btc_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        price = data['bpi']['USD']['rate']
        return f"The current price of Bitcoin is ${price}"
    except Exception as e:
        return f"Error fetching Bitcoin price: {e}"

# Function to update the price label
def update_price_label():
    price = get_btc_price()
    price_label.config(text=price)

# Create the main window
root = tk.Tk()
root.title("Bitcoin Price Tracker")

# Create and configure the label to display the price
price_label = tk.Label(root, font=('Arial', 14))
price_label.pack(pady=20)
update_price_label()  # Initial update

# Create and configure the update button
update_button = tk.Button(root, text="Update Price", command=update_price_label)
update_button.pack()

# Function to show an error message
def show_error():
    messagebox.showerror("Error", "Failed to fetch Bitcoin price")

# Create and configure the error button
error_button = tk.Button(root, text="Show Error", command=show_error)
error_button.pack()

# Function to close the application
def close_app():
    root.destroy()

# Create and configure the close button
close_button = tk.Button(root, text="Close", command=close_app)
close_button.pack()

# Run the Tkinter event loop
root.mainloop()
