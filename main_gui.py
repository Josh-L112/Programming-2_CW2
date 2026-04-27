import tkinter as tk
from tkinter import messagebox
from scheduler import Scheduler
from file_handler import load_data, save_data

# load data
bookings = load_data("bookings.json")
scheduler = Scheduler(bookings)

# window setup
root = tk.Tk()
root.title("UniScheduler")
root.geometry("450x450")
root.configure(bg="#f4f4f4")


# ===== FUNCTIONS =====

def add_booking():
    resource = resource_var.get()
    user = user_entry.get()
    time = time_entry.get()

    try:
        capacity = int(capacity_entry.get())
    except:
        messagebox.showerror("Error", "Capacity must be a number")
        return

    success = scheduler.add_booking(resource, user, time, capacity)

    if success:
        messagebox.showinfo("Success", "Booking added successfully")
        clear_fields()
        view_bookings()
    else:
        messagebox.showerror("Error", "Booking failed (conflict or capacity issue)")


def view_bookings():
    bookings_list.delete(0, tk.END)

    for b in scheduler.get_bookings():
        text = f"{b['resource']} | {b['user']} | {b['time']} | {b['capacity']}"
        bookings_list.insert(tk.END, text)


def clear_fields():
    user_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    capacity_entry.delete(0, tk.END)


def on_exit():
    save_data("bookings.json", scheduler.get_bookings())
    root.destroy()


# ===== UI LAYOUT =====

title = tk.Label(root, text="UniScheduler", font=("Arial", 16), bg="#f4f4f4")
title.pack(pady=10)

form_frame = tk.Frame(root, bg="#f4f4f4")
form_frame.pack(pady=10)

# Resource dropdown
tk.Label(form_frame, text="Resource:", bg="#f4f4f4").grid(row=0, column=0, sticky="w")
resource_var = tk.StringVar()
resource_var.set("RoomA")
resource_menu = tk.OptionMenu(form_frame, resource_var, "RoomA", "Lab1")
resource_menu.grid(row=0, column=1, padx=10, pady=5)

# User input
tk.Label(form_frame, text="User:", bg="#f4f4f4").grid(row=1, column=0, sticky="w")
user_entry = tk.Entry(form_frame)
user_entry.grid(row=1, column=1, padx=10, pady=5)

# Time input
tk.Label(form_frame, text="Time:", bg="#f4f4f4").grid(row=2, column=0, sticky="w")
time_entry = tk.Entry(form_frame)
time_entry.grid(row=2, column=1, padx=10, pady=5)

# Capacity input
tk.Label(form_frame, text="Capacity:", bg="#f4f4f4").grid(row=3, column=0, sticky="w")
capacity_entry = tk.Entry(form_frame)
capacity_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Booking", width=15, command=add_booking).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="View Bookings", width=15, command=view_bookings).grid(row=0, column=1, padx=5)

# Listbox
bookings_list = tk.Listbox(root, width=55)
bookings_list.pack(pady=10)

# Exit button
tk.Button(root, text="Save & Exit", command=on_exit).pack(pady=10)


# run app
root.mainloop()