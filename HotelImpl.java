import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;

/**
 * Implementation of the HotelInterface.
 * Manages the state of hotel rooms on the server.
 */
public class HotelImpl extends UnicastRemoteObject implements HotelInterface {
    private HashMap<Integer, String> rooms;

    protected HotelImpl() throws RemoteException {
        super();
        rooms = new HashMap<>();
        // Initialize 10 rooms
        for (int i = 101; i <= 110; i++) {
            rooms.put(i, "Available");
        }
    }

    @Override
    public String bookRoom(String guestName, int roomNumber) throws RemoteException {
        if (!rooms.containsKey(roomNumber)) return "Error: Room " + roomNumber + " does not exist.";
        if (!rooms.get(roomNumber).equals("Available")) {
            return "Error: Room " + roomNumber + " is already occupied by " + rooms.get(roomNumber);
        }
        
        rooms.put(roomNumber, guestName);
        return "Success: Room " + roomNumber + " has been booked for " + guestName;
    }

    @Override
    public String cancelBooking(int roomNumber) throws RemoteException {
        if (!rooms.containsKey(roomNumber)) return "Error: Room " + roomNumber + " does not exist.";
        if (rooms.get(roomNumber).equals("Available")) {
            return "Error: Room " + roomNumber + " is already available.";
        }
        
        String guest = rooms.get(roomNumber);
        rooms.put(roomNumber, "Available");
        return "Success: Booking for " + guest + " in Room " + roomNumber + " has been cancelled.";
    }

    @Override
    public HashMap<Integer, String> getStatus() throws RemoteException {
        return rooms;
    }
}
