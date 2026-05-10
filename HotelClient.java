import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;
import java.util.HashMap;

/**
 * Client application to interact with the Hotel RMI Server.
 */
public class HotelClient {
    public static void main(String[] args) {
        try {
            // Connect to the RMI registry on localhost
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            
            // Look up the remote object by its registered name
            HotelInterface stub = (HotelInterface) registry.lookup("HotelService");
            
            Scanner sc = new Scanner(System.in);
            System.out.println("Connected to Hotel Booking Server.");

            while (true) {
                System.out.println("\n--- HOTEL RMI MENU ---");
                System.out.println("1. View Room Status");
                System.out.println("2. Book Room");
                System.out.println("3. Cancel Booking");
                System.out.println("4. Exit");
                System.out.print("Enter choice: ");
                
                int choice = sc.nextInt();
                if (choice == 4) {
                    System.out.println("Exiting Client...");
                    break;
                }

                switch (choice) {
                    case 1:
                        HashMap<Integer, String> status = stub.getStatus();
                        System.out.println("\nCurrent Hotel Status:");
                        status.forEach((room, guest) -> 
                            System.out.println("Room " + room + ": " + guest)
                        );
                        break;
                        
                    case 2:
                        System.out.print("Enter Guest Name: ");
                        String name = sc.next();
                        System.out.print("Enter Room Number (101-110): ");
                        int room = sc.nextInt();
                        System.out.println("\n[Server]: " + stub.bookRoom(name, room));
                        break;
                        
                    case 3:
                        System.out.print("Enter Room Number to Cancel: ");
                        int cRoom = sc.nextInt();
                        System.out.println("\n[Server]: " + stub.cancelBooking(cRoom));
                        break;
                        
                    default:
                        System.out.println("Invalid choice.");
                }
            }
            sc.close();
        } catch (Exception e) {
            System.err.println("Client Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
