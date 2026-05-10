from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# The service class containing the concatenation logic
class StringService:
    def concatenate(self, str1, str2):
        """Remotely joins two strings together with a space in between."""
        return f"{str1} {str2}"

# Customizing the URL path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Initialize the server
with SimpleXMLRPCServer(('localhost', 5000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    server.register_instance(StringService())
    
    print("RMI-style String Server is running on port 5000...")
    server.serve_forever()