from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, data):
        encrypted_data = self.cipher_suite.encrypt(data)
        return encrypted_data, self.key
