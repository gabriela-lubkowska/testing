import socket
import os

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return f'Twoje IP: {ip_address}'

def check_proxy():
    proxy = os.environ.get('http_proxy')
    if proxy:
        return f'Proxy enabled: {proxy}'
    else:
        return 'No proxy configured.'