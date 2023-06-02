import tkinter as tk
from tkinter import messagebox

class Gift:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class ParkareTo:
    def __init__(self):
        self.gifts = []
        self.root = tk.Tk()
        self.root.title("ParkareTo")

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.description_label = tk.Label(self.root, text="Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack()

        self.price_label = tk.Label(self.root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(self.root)
        self.price_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.add_gift)
        self.submit_button.pack()

    def add_gift(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        price = float(self.price_entry.get())

        gift = Gift(name, description, price)
        self.gifts.append(gift)
        messagebox.showinfo("Gift Added", "Gift added successfully!")

        self.name_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def get_gifts(self):
        if len(self.gifts) == 0:
            messagebox.showinfo("No Gifts", "No gifts found.")
        else:
            gift_info = "Gifts:\n"
            for gift in self.gifts:
                gift_info += f"Name: {gift.name}\n"
                gift_info += f"Description: {gift.description}\n"
                gift_info += f"Price: {gift.price}\n"
                gift_info += "\n"

            messagebox.showinfo("Gifts", gift_info)

    def run(self):
        self.root.mainloop()

# Creating an instance of the ParkingApp
parkare_to = ParkareTo()

# Running the app
parkare_to.run()
