# Base class for all resources
class Resource:
    def __init__(self, resource_id, location, capacity):
        self._resource_id = resource_id   # protected variable
        self._location = location
        self._capacity = capacity

    def get_capacity(self):
        return self._capacity

    def get_details(self):
        return f"{self._resource_id} at {self._location}"


# Inherits from Resource
class LabSpace(Resource):
    def __init__(self, resource_id, location, capacity, computers):
        super().__init__(resource_id, location, capacity)
        self.computers = computers

    # polymorphism (overriding method)
    def get_details(self):
        return f"Lab {self._resource_id} | PCs: {self.computers}"


# Another subclass
class MeetingRoom(Resource):
    def __init__(self, resource_id, location, capacity, projector):
        super().__init__(resource_id, location, capacity)
        self.projector = projector

    def get_details(self):
        return f"Room {self._resource_id} | Projector: {self.projector}"