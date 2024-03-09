import tkinter as tk

def on_button_click(button_num):
    print(f"Button {button_num} clicked")
    # Add your function to perform when a button is clicked
    root.after_cancel(timeout_id)  # Cancel the scheduled window destruction

def destroy_window():
    print("No button clicked. Destroying window.")
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Button Click Checker")

# Set up a timer to destroy the window if no button is clicked within 5 seconds
timeout_id = root.after(5000, destroy_window)

# Create three buttons
button1 = tk.Button(root, text="Button 1", command=lambda: on_button_click(1))
button2 = tk.Button(root, text="Button 2", command=lambda: on_button_click(2))
button3 = tk.Button(root, text="Button 3", command=lambda: on_button_click(3))

# Pack the buttons
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# Close the main window
root.mainloop()
