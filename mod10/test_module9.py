# test_module9.py

import unittest
import threading
import time
import socket
import socketserver
from networking_operations import get_local_ip, create_tcp_server, create_tcp_client, create_udp_server, create_udp_client

class TCPServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        pass

class TestNetworkingOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start TCP server in a separate thread
        cls.host, cls.port = "127.0.0.1", 12345
        cls.server_socket = create_tcp_server(cls.host, cls.port)
        cls.server_thread = threading.Thread(target=cls.server_socket.accept)
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(0.1)  # Give some time for the server to start

    @classmethod
    def tearDownClass(cls):
        try:
            # Close the TCP server if it is still open
            if cls.server_socket.fileno() != -1:
                cls.server_socket.close()
                # Print message indicating the server socket was closed
                print("Server socket closed")
            else:
                # Print message indicating the server socket was already closed
                print("Server socket was already closed")
        except Exception as e:
            # Handle any exceptions during server socket closure
            print("Error while closing server socket:", e)

    def tearDown(self):
        # Check if the server socket is open before closing it
        if self.server_socket.fileno() != -1:
            self.server_socket.close()
            # Print message indicating the client connection was closed
            print("Client connection successfully closed")

        # Check if the UDP client socket is open before closing it
        if hasattr(self, 'udp_client_socket') and self.udp_client_socket.fileno() != -1:
            self.udp_client_socket.close()
            # Print message indicating the UDP client connection was closed
            print("UDP client connection successfully closed")

    def test_get_local_ip(self):
        local_ip = get_local_ip()
        self.assertTrue(socket.inet_aton(local_ip))

    def test_create_tcp_server_and_client(self):
        # Test TCP client
        client_socket = create_tcp_client(self.host, self.port)
        self.assertIsNotNone(client_socket)
        client_socket.close()

    def test_create_udp_server_and_client(self):
        host, port = "127.0.0.1", 12345

        # Test UDP server
        server_socket = create_udp_server(host, port)
        self.assertIsNotNone(server_socket)
        server_socket.close()

        # Test UDP client
        self.udp_client_socket = create_udp_client()
        self.assertIsNotNone(self.udp_client_socket)
        self.udp_client_socket.close()

if __name__ == "__main__":
    unittest.main()
