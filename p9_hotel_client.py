import xmlrpc.client

def run_client():
    """
    Client application for the Distributed Hotel Booking System.
    Connects to the XML-RPC server to book or cancel rooms.
    """
    # URL of the Hotel Server
    server_url = "http://localhost:8000/"
    
    try:
        # Create a proxy object to the server
        proxy = xmlrpc.client.ServerProxy(server_url)
        print(f"Successfully connected to Hotel Server at {server_url}")

        while True:
            print("\n" + "="*30)
            print("  HOTEL BOOKING SYSTEM (RPC)")
            print("="*30)
            print("1. View All Room Status")
            print("2. Book a Room for Guest")
            print("3. Cancel a Booking")
            print("4. Exit")
            
            choice = input("\nEnter choice (1-4): ")
            
            if choice == '1':
                # Invoke the remote get_status method
                status = proxy.get_status()
                print("\nCURRENT ROOM AVAILABILITY:")
                for room, guest in sorted(status.items()):
                    print(f"Room {room}: {guest}")
            
            elif choice == '2':
                name = input("Enter Guest Name: ")
                room = input("Enter Room Number (101-110): ")
                # Invoke the remote book_room method
                response = proxy.book_room(name, room)
                print(f"\n[Server Response]: {response}")
                
            elif choice == '3':
                room = input("Enter Room Number to cancel: ")
                # Invoke the remote cancel_booking method
                response = proxy.cancel_booking(room)
                print(f"\n[Server Response]: {response}")
                
            elif choice == '4':
                print("Exiting Client Application...")
                break
            else:
                print("Invalid input! Please enter a number between 1 and 4.")

    except ConnectionRefusedError:
        print("\n[ERROR]: Could not connect to the server.")
        print("Ensure 'hotel_server.py' is running on port 8000 before starting the client.")
    except Exception as e:
        print(f"\n[ERROR]: {e}")

if __name__ == "__main__":
    run_client()
