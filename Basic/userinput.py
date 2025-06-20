import tkinter as tk

# Initialize the user_input variable outside the function so it can be accessed later
user_input = ""

def get_and_store_input():
    global user_input # Use the global keyword to modify the user_input variable
    # Get all text from the Text widget, from the beginning ("1.0") to the end ("end")
    # "end-1c" removes the trailing newline character that Text widgets add
    user_input = text_entry.get("1.0", "end-1c")
    window.destroy()  # Close the window after getting input

# Create the main window
window = tk.Tk()
window.title("User Input")

# Configure the window to be resizable
# Passing True for both width and height makes the window resizable in both directions
window.resizable(True, True)

# Create a label
label = tk.Label(window, text="prompt:")
label.pack()

# Create a Text widget for multi-line input
# You can adjust the height and width to control the initial size
text_entry = tk.Text(window, height=30, width=80)
text_entry.pack(expand=True, fill='both') # Allow the Text widget to expand and fill the window

# Create a button to submit the input
submit_button = tk.Button(window, text="Submit", command=get_and_store_input)
submit_button.pack()

# Start the Tkinter event loop - This makes the window appear
window.mainloop()
