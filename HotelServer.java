import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

/**
 * Main Server class to host the Hotel Booking Service.
 */
public class HotelServer {
    public static void main(String[] args) {
        try {
            // Create the remote object
            HotelImpl obj = new HotelImpl();
            
            // Create and start the RMI registry on default port 1099
            Registry registry = LocateRegistry.createRegistry(1099);
            
            // Bind the remote object to a name in the registry
            registry.rebind("HotelService", obj);
            
            System.out.println("====================================");
            System.out.println("Hotel Booking RMI Server is Ready");
            System.out.println("====================================");
        } catch (Exception e) {
            System.err.println("Server Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
