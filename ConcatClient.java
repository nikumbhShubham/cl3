import java.rmi.*;
import java.util.*;

/**
 * Client class to invoke the remote concatenation method.
 */
public class ConcatClient {
    public static void main(String args[]) {
        try {
            // Lookup the remote object from the RMI registry
            ConcatInterface stub = (ConcatInterface)Naming.lookup("rmi://localhost/ConcatService");
            
            Scanner sc = new Scanner(System.in);
            System.out.println("=== P2: RMI String Concatenation ===");
            System.out.print("Enter String 1: ");
            String s1 = sc.nextLine();
            System.out.print("Enter String 2: ");
            String s2 = sc.nextLine();
            
            // Invoke the remote method
            String result = stub.concatenate(s1, s2);
            System.out.println("\nServer Response: " + result);
            
            sc.close();
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
