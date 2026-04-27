import tkinter as tk
from tkinter import messagebox
from scheduler import Scheduler
from file_handler import load_data, save_data

# load existing bookings
bookings = load_data("bookings.json")
scheduler = Scheduler(bookings)

# main window
root = tk.Tk()
root.title("UniScheduler")
root.geometry("400x400")


# ===== FUNCTIONS =====

def add_booking():
    resource = resource_entry.get()
    user = user_entry.get()
    time = time_entry.get()

    try:
        capacity = int(capacity_entry.get())
    except:
        messagebox.showerror("Error", "Capacity must be a number")
        return

    success = scheduler.add_booking(resource, user, time, capacity)

    if success:
        messagebox.showinfo("Success", "Booking added")
        clear_fields()
    else:
        messagebox.showerror("Error", "Booking failed (conflict or capacity issue)")


def view_bookings():
    bookings_list.delete(0, tk.END)

    for b in scheduler.get_bookings():
        text = f"{b['resource']} | {b['user']} | {b['time']} | {b['capacity']}"
        bookings_list.insert(tk.END, text)


def clear_fields():
    resource_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    capacity_entry.delete(0, tk.END)


def on_exit():
    save_data("bookings.json", scheduler.get_bookings())
    root.destroy()


# ===== UI LAYOUT =====

tk.Label(root, text="Resource (RoomA / Lab1)").pack()
resource_entry = tk.Entry(root)
resource_entry.pack()

tk.Label(root, text="User Name").pack()
user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root, text="Time (e.g 10:00)").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Label(root, text="Capacity").pack()
capacity_entry = tk.Entry(root)
capacity_entry.pack()

tk.Button(root, text="Add Booking", command=add_booking).pack(pady=5)
tk.Button(root, text="View Bookings", command=view_bookings).pack(pady=5)

bookings_list = tk.Listbox(root, width=50)
bookings_list.pack(pady=10)

tk.Button(root, text="Exit", command=on_exit).pack(pady=5)

# run app
root.mainloop()