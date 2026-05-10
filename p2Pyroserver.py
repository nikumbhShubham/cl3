import Pyro4

@Pyro4.expose  # Explicitly allow this class to be remote
class StringService:
    def concatenate(self, s1, s2):
        return s1 + s2

daemon = Pyro4.Daemon()                # make a Pyro daemon
uri = daemon.register(StringService)   # register the class as a Pyro object

print(f"Ready. Object URI = {uri}")    # You have to give this long string to the client
daemon.requestLoop()                   # start the event loop
