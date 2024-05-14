import tkinter as tk
from tkinter import filedialog
from .file_handler import FileHandler
from .encryptor import Encryptor
import socket

class ClientGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Client Application")
        
        self.file_label = tk.Label(self.root, text="Select a file")
        self.file_label.pack()
        
        self.file_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.file_button.pack()
        
        self.transmission_type = tk.StringVar(value="json")
        self.binary_radio = tk.Radiobutton(self.root, text="Binary", variable=self.transmission_type, value="binary")
        self.json_radio = tk.Radiobutton(self.root, text="JSON", variable=self.transmission_type, value="json")
        self.xml_radio = tk.Radiobutton(self.root, text="XML", variable=self.transmission_type, value="xml")
        
        self.binary_radio.pack()
        self.json_radio.pack()
        self.xml_radio.pack()
        
        self.encrypt_var = tk.IntVar()
        self.encrypt_check = tk.Checkbutton(self.root, text="Encrypt", variable=self.encrypt_var)
        self.encrypt_check.pack()
        
        self.send_button = tk.Button(self.root, text="Send", command=self.send_file)
        self.send_button.pack()
        
        self.file_path = None

    def browse_file(self):
        self.file_path = filedialog.askopenfilename()
        self.file_label.config(text=f"Selected file: {self.file_path}")

    def send_file(self):
        if not self.file_path:
            print("No file selected")
            return
        
        handler = FileHandler(self.file_path)
        data_format = self.transmission_type.get()
        data = handler.serialise(data_format)
        
        encrypted = self.encrypt_var.get()
        if encrypted:
            encryptor = Encryptor()
            data, key = encryptor.encrypt(data)
        else:
            key = None
        
        self.send_to_server(data, data_format, encrypted, key)

    def send_to_server(self, data, data_format, encrypted, key):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9999))
        client_socket.sendall(data_format.encode())
        client_socket.sendall(str(encrypted).encode())
        client_socket.sendall(key if key else b'')
        client_socket.sendall(data)
        client_socket.close()

    def run(self):
        self.root.mainloop()

