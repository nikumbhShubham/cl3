import java.rmi.*;
import java.rmi.registry.*;

/**
 * Server class to host the String Concatenation Service.
 */
public class ConcatServer {
    public static void main(String args[]) {
        try {
            ConcatImpl obj = new ConcatImpl();
            // Programmatically start the RMI registry on default port 1099
            LocateRegistry.createRegistry(1099);
            // Rebind the service to the registry
            Naming.rebind("ConcatService", obj);
            System.out.println("P2: String Concatenation Server is running on port 1099...");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
