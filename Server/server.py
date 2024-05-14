import socket
import json
import xml.etree.ElementTree as ET
import pickle
import os
from Server.logger import setup_logging
from Server.config import Config
from cryptography.fernet import Fernet

# Setup logging
logger = setup_logging()

def deserialise_data(data, data_format):
    if data_format == 'json':
        return json.loads(data)
    elif data_format == 'xml':
        root = ET.fromstring(data)
        return {child.tag: child.text for child in root}
    elif data_format == 'binary':
        return pickle.loads(data)
    else:
        raise ValueError("Unsupported data format")

def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data

def main():
    config = Config()
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((config.host, config.port))
    server_socket.listen(5)
    logger.info(f'Server started on {config.host}:{config.port}')

    while True:
        client_socket, addr = server_socket.accept()
        logger.info(f'Connection from {addr}')
        data_format = client_socket.recv(1024).decode()
        encrypted = client_socket.recv(1024).decode() == 'True'
        key = client_socket.recv(1024) if encrypted else None
        data = client_socket.recv(1024)
        
        if encrypted:
            data = decrypt_data(data, key)
        
        data = deserialise_data(data, data_format)
        logger.info(f'Received data: {data}')
        
        client_socket.close()

if __name__ == "__main__":
    main()
