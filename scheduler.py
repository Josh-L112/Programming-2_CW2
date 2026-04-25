class Scheduler:
    def __init__(self, bookings):
        self.bookings = bookings

    def add_booking(self, resource, user, time, capacity):
        # conflict check
        for b in self.bookings:
            if b["resource"] == resource and b["time"] == time:
                return False

        new_booking = {
            "resource": resource,
            "user": user,
            "time": time,
            "capacity": capacity
        }

        self.bookings.append(new_booking)
        return True

    def get_bookings(self):
        return self.bookings