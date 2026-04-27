# Handles all booking logic
class Scheduler:
    def __init__(self, bookings):
        self.bookings = bookings

        # simple resource list (could be expanded)
        self.resources = {
            "RoomA": 20,
            "Lab1": 30
        }

    # check if booking clashes
    def check_conflict(self, resource, time):
        for b in self.bookings:
            if b["resource"] == resource and b["time"] == time:
                return True
        return False

    # check if capacity is allowed
    def check_capacity(self, resource, capacity):
        if resource in self.resources:
            return capacity <= self.resources[resource]
        return False

    # add booking
    def add_booking(self, resource, user, time, capacity):

        # check if resource exists
        if resource not in self.resources:
            print("Resource does not exist.")
            return False

        # check for clash
        if self.check_conflict(resource, time):
            return False

        # check capacity
        if not self.check_capacity(resource, capacity):
            return False

        # create booking
        booking = {
            "resource": resource,
            "user": user,
            "time": time,
            "capacity": capacity
        }

        self.bookings.append(booking)
        return True

    def get_bookings(self):
        return self.bookings