from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RPCServer:
    def calculate_factorial(self, n):
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/api/v1/rpc_handler',)

with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions() 
    server.register_instance(RPCServer())
    print("FactorialServer is ready to accept requests.")
    server.serve_forever()