# networking_operations.py

import socket

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def create_tcp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"TCP server started at {host}:{port}")
    return server_socket

def create_tcp_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"TCP client connected to server {host}:{port}")
    return client_socket

def create_udp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP server started at {host}:{port}")
    return server_socket

def create_udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("UDP client created")
    return client_socket

