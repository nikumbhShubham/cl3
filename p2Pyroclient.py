import Pyro4

uri = input("Enter the URI from the server: ")
proxy = Pyro4.Proxy(uri)
print(proxy.concatenate("Hello", "World"))
