import random
from collections import Counter
import tkinter as tk

def generate_and_display_result():
    # Generate 100,000 random 1s and 0s
    random_bits = [random.randint(0, 1) for _ in range(100000)]

    # Count the occurrences of 0s and 1s
    counts = Counter(random_bits)

    # Find the value with the highest occurrence
    most_common_value = counts.most_common(1)[0]

    # Format the result text
    result = f"Value: {most_common_value[0]}, Occurrences: {most_common_value[1]}"
    
    # Insert the result into the listbox
    results_listbox.insert(tk.END, result)

    # Highlight the latest result
    results_listbox.itemconfig(tk.END, {'bg': 'yellow', 'fg': 'black'})

    # Clear previous highlight
    if results_listbox.size() > 1:
        results_listbox.itemconfig(results_listbox.size() - 2, {'bg': 'white', 'fg': 'black'})

# Create the main window
root = tk.Tk()
root.title("Random Bit Generator")

# Create a button to generate random bits and find the most common value
generate_button = tk.Button(
    root, 
    text="Generate and Find Most Common Value", 
    command=generate_and_display_result, 
    padx=20, pady=10
)

# Create a listbox to display the history of results
results_listbox = tk.Listbox(root, width=50, height=10)

# Pack the button and listbox into the window
generate_button.pack(pady=10)
results_listbox.pack(pady=10)

# Run the GUI event loop
root.mainloop()
