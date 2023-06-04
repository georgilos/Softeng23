import tkinter as tk
from tkinter import messagebox

def show_message():
    answer1 = entry1.get()
    messagebox.showinfo("AI Support", f"Hello, {answer1} !")

def submit_answer():
    answer1 = entry1.get()
    answer2 = entry2.get()
    messagebox.showinfo("AI Support", f"Hi {answer1} \n Someone of our Membership try to fix the problem which is : {answer2}")

# Create a new tkinter window
window = tk.Tk()
window.title("AI Support")

# Create a label widget for messages
message_label = tk.Label(window, text="Welcome to the AI Support of PARKARE TO!")
message_label.pack(pady=10)

# Create a label widget for the first question
question1_label = tk.Label(window, text="What is your username?")
question1_label.pack()

# Create a text entry widget for the first question
entry1 = tk.Entry(window)
entry1.pack(pady=5)

# Create a label widget for the second question
question2_label = tk.Label(window, text="How can i help you?")
question2_label.pack()

# Create a text entry widget for the second question
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Create a button widget for submitting the answers
submit_button = tk.Button(window, text="Submit", command=submit_answer)
submit_button.pack(pady=5)



# Run the tkinter event loop
window.mainloop()