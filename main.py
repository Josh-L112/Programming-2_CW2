from scheduler import Scheduler
from file_handler import load_data, save_data

def display_menu():
    print("\n===== UniScheduler =====")
    print("1. Add Booking")
    print("2. View Bookings")
    print("3. Exit")


def main():
    # Load existing bookings
    bookings = load_data("bookings.json")

    scheduler = Scheduler(bookings)

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # OPTION 1: Add booking
        if choice == 1:
            resource = input("Enter resource name: ")
            user = input("Enter your name: ")
            time = input("Enter time (e.g. 10:00): ")
            capacity = input("Enter required capacity: ")

            try:
                capacity = int(capacity)
            except ValueError:
                print("Capacity must be a number.")
                continue

            success = scheduler.add_booking(resource, user, time, capacity)

            if success:
                print("Booking added successfully.")
            else:
                print("Booking failed (conflict or capacity issue).")

        # OPTION 2: View bookings
        elif choice == 2:
            all_bookings = scheduler.get_bookings()

            if not all_bookings:
                print("No bookings found.")
            else:
                print("\n--- Bookings ---")
                for b in all_bookings:
                    print(f"{b['resource']} | {b['user']} | {b['time']} | Capacity: {b['capacity']}")

        # OPTION 3: Exit
        elif choice == 3:
            save_data("bookings.json", scheduler.get_bookings())
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()