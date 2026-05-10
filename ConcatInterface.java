import java.rmi.*;

/**
 * Remote Interface for P2 String Concatenation.
 */
public interface ConcatInterface extends Remote {
    public String concatenate(String s1, String s2) throws RemoteException;
}
