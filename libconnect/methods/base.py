import ipaddress
import socket


class BaseMethod:
    """Base abstract class for connection methods."""

    def client_init(self) -> bool:
        "Called by the client to initialize this connection (opens ports etc). Returns True on success."
        return False

    def connect_to(self, ip: ipaddress) -> socket:
        "Tries to connect to client on ip. Returns a socket."
        return None
