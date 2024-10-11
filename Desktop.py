import tkinter as tk
import subprocess

# Function to handle button clicks
def button_click():
    text = entry.get()
    label.config(text=f"You entered: {text}")

    if checkbox.get():
        label.config(fg="blue")
    else:
        label.config(fg="black")

    selected_option = var.get()
    label.config(text=f"You selected: {options[selected_option - 1]}")

def open_cmd_window():
    subprocess.Popen(["cmd"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def open_custom_terminal():
    new_window = tk.Toplevel()
    new_window.title("Custom Terminal")
    new_window.geometry("800x600")

    terminal_text = tk.Text(new_window, wrap=tk.WORD, bg="black", fg="white")
    terminal_text.pack(fill=tk.BOTH, expand=True)

    process = subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    def on_key_press(event):
        process.stdin.write(event.char.encode())
        process.stdin.flush()
        terminal_text.focus_set()

    terminal_text.bind("<Key>", on_key_press)

    while True:
        output = process.stdout.readline().decode("utf-8").rstrip()
        if output == "":
            break
        terminal_text.insert(tk.END, output + "\n")
        terminal_text.see(tk.END)

# Create the main window
window = tk.Tk()

# Create a button with the "Open Terminal" functionality
button_terminal = tk.Button(window, text="Open Terminal", command=open_custom_terminal)
button_terminal.grid(row=0, column=0, sticky="w")

# Create a label
label = tk.Label(window, text="Hello, world!", font=("Arial", 12, "bold"))
label.grid(row=0, column=1, sticky="w")

# Create a text entry field
entry = tk.Entry(window)
entry.grid(row=1, column=1, sticky="w")

# Create a checkbox
checkbox = tk.Checkbutton(window, text="Check me")
checkbox.grid(row=2, column=1, sticky="w")

# Create radio buttons
var = tk.IntVar()
radio1 = tk.Radiobutton(window, text="Option 1", variable=var, value=1)
radio2 = tk.Radiobutton(window, text="Option 2", variable=var, value=2)
radio1.grid(row=3, column=1, sticky="w")
radio2.grid(row=4, column=1, sticky="w")

# Create a drop-down menu
options = ["Option A", "Option B", "Option C"]
dropdown = tk.OptionMenu(window, var, *options)
dropdown.grid(row=5, column=1, sticky="w")

# Separate button for handling other functionalities
button = tk.Button(window, text="Click Me!", command=button_click)
button.grid(row=6, column=1, sticky="w")

# Create buttons for opening the command prompt and custom terminal
button_cmd = tk.Button(window, text="Open Command Prompt", command=open_cmd_window)
button_cmd.grid(row=7, column=1, sticky="w")

# Start the event loop
window.mainloop()