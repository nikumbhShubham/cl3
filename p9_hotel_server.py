from xmlrpc.server import SimpleXMLRPCServer

class HotelBookingSystem:
    def __init__(self):
        # Initializing room data: {room_number: guest_name}
        self.rooms = {}
        for i in range(101, 111):
            self.rooms[str(i)] = "Available"

    def book_room(self, guest_name, room_number):
        """Remotely registers a guest to a specific room."""
        room_number = str(room_number)
        if room_number not in self.rooms:
            return "Error: Room does not exist."
        
        if self.rooms[room_number] != "Available":
            return f"Error: Room {room_number} is already occupied by {self.rooms[room_number]}."
        
        self.rooms[room_number] = guest_name
        return f"Success: Room {room_number} booked for {guest_name}."

    def cancel_booking(self, room_number):
        """Remotely removes a booking and makes the room available again."""
        room_number = str(room_number)
        if room_number not in self.rooms:
            return "Error: Room does not exist."
        
        if self.rooms[room_number] == "Available":
            return f"Error: Room {room_number} is already available."
        
        guest = self.rooms[room_number]
        self.rooms[room_number] = "Available"
        return f"Success: Booking for {guest} in Room {room_number} has been cancelled."

    def get_status(self):
        """Returns the current status of all rooms."""
        return self.rooms

# Server Setup
if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(HotelBookingSystem())
    print("Hotel Booking Server (RMI Style) is active on port 8000...")
    server.serve_forever()
