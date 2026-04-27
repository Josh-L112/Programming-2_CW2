# Simple booking class
class Booking:
    def __init__(self, resource, user, time, capacity):
        self.resource = resource
        self.user = user
        self.time = time
        self.capacity = capacity

    # convert to dictionary for saving
    def to_dict(self):
        return {
            "resource": self.resource,
            "user": self.user,
            "time": self.time,
            "capacity": self.capacity
        }

    def __str__(self):
        return f"{self.resource} | {self.user} | {self.time} | {self.capacity}"