import tkinter as tk
from time import strftime

def update_time():
    time_string = strftime('%H:%M:%S %p')
    label.config(text=time_string)
    label.after(1000, update_time)  # Schedule the next update after 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock"
           " by Kutman")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='red')
label.pack(pady=0)

# Start the clock update
update_time()

# Run the main event loop
root.mainloop()

