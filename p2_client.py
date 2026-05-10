import xmlrpc.client

# Connect to the server on port 5000
with xmlrpc.client.ServerProxy("http://localhost:5000/RPC2") as proxy:
    try:
        print("--- Distributed String Concatenation ---")
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")
        
        # Remote call to the server
        result = proxy.concatenate(s1, s2)
        
        print("\n[Server Response]")
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"Error during RMI: {e}")