import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.HashMap;

/**
 * Remote Interface for the Hotel Booking System.
 * Defines the methods that can be invoked by the client.
 */
public interface HotelInterface extends Remote {
    String bookRoom(String guestName, int roomNumber) throws RemoteException;
    String cancelBooking(int roomNumber) throws RemoteException;
    HashMap<Integer, String> getStatus() throws RemoteException;
}
