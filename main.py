import tkinter as tk  # Import the tkinter module for GUI
import subprocess  # Import the subprocess module to run system commands

def tracert_command():
    url = url_entry.get()
    output_text.delete(1.0, tk.END)
    # Using traceroute instead of tracert
    traceroute = subprocess.Popen(["traceroute", url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in traceroute.stdout:
        output_text.insert(tk.END, line)

def nslookup_command():
    url = url_entry.get()  # Get the URL entered in the entry field
    output_text.delete(1.0, tk.END)  # Clear previous output from the text box
    # Execute the nslookup command with the specified URL
    nslookup = subprocess.Popen(["nslookup", url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    # Read the output of the command line by line and insert it into the text box
    for line in nslookup.stdout:
        output_text.insert(tk.END, line)

def ping_command():
    url = url_entry.get()  # Get the URL entered in the entry field
    output_text.delete(1.0, tk.END)  # Clear previous output from the text box
    # Execute the ping command with the specified URL
    ping = subprocess.Popen(["ping", url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    # Read the output of the command line by line and insert it into the text box
    for line in ping.stdout:
        output_text.insert(tk.END, line)

def save_command():
    with open("output.txt", "w") as file:  # Open a file named "output.txt" in write mode
        # Write the content of the text box into the file
        file.write(output_text.get(1.0, tk.END))

# Create the main window of the application
root = tk.Tk()
root.title("Network Utility")  # Set the title of the window

# Create a label and an entry field for entering the URL
url_label = tk.Label(root, text="Enter URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = tk.Entry(root)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Create buttons for "Tracert", "Nslookup", "Ping", and "Save" functionalities
tracert_button = tk.Button(root, text="Tracert", command=tracert_command)
tracert_button.grid(row=1, column=0, padx=5, pady=5)

nslookup_button = tk.Button(root, text="Nslookup", command=nslookup_command)
nslookup_button.grid(row=1, column=1, padx=5, pady=5)

ping_button = tk.Button(root, text="Ping", command=ping_command)
ping_button.grid(row=1, column=2, padx=5, pady=5)

save_button = tk.Button(root, text="Save", command=save_command)
save_button.grid(row=1, column=3, padx=5, pady=5)

# Create a text box for displaying the output
output_text = tk.Text(root, wrap="word", width=50, height=20)
output_text.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()  # Start the event loop of the GUI
