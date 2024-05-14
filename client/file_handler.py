import json
import xml.etree.ElementTree as ET
import pickle

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def serialize(self, data_format):
        data = self.read_file()
        if data_format == 'json':
            return json.dumps(data).encode()
        elif data_format == 'xml':
            root = ET.Element("root")
            child = ET.SubElement(root, "data")
            child.text = data
            return ET.tostring(root)
        elif data_format == 'binary':
            return pickle.dumps(data)
        else:
            raise ValueError("Unsupported data format")
