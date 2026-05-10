import java.rmi.*;
import java.rmi.server.*;

/**
 * Implementation of the String Concatenation logic.
 */
public class ConcatImpl extends UnicastRemoteObject implements ConcatInterface {
    public ConcatImpl() throws RemoteException {
        super();
    }

    @Override
    public String concatenate(String s1, String s2) {
        return s1 + " " + s2;
    }
}
