from scheduler import Scheduler
from file_handler import load_data, save_data

def menu():
    print("\n--- UniScheduler ---")
    print("1. Add booking")
    print("2. View bookings")
    print("3. Exit")

def main():
    bookings = load_data("bookings.json")
    scheduler = Scheduler(bookings)

    while True:
        menu()

        try:
            choice = int(input("Choose option: "))
        except:
            print("Invalid input, try again.")
            continue

        if choice == 1:
            resource = input("Enter room (RoomA / Lab1): ")
            user = input("Enter your name: ")
            time = input("Enter time (e.g 10:00): ")

            try:
                capacity = int(input("Enter number of people: "))
            except:
                print("Capacity must be a number.")
                continue

            # try to add booking
            success = scheduler.add_booking(resource, user, time, capacity)

            if success:
                print("Booking successful.")
            else:
                print("Booking failed (conflict or capacity issue).")

        elif choice == 2:
            bookings = scheduler.get_bookings()

            if len(bookings) == 0:
                print("No bookings yet.")
            else:
                print("\nBookings:")
                for b in bookings:
                    print(f"{b['resource']} | {b['user']} | {b['time']} | {b['capacity']}")

        elif choice == 3:
            save_data("bookings.json", scheduler.get_bookings())
            print("Saved. Goodbye.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()