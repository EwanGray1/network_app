import unittest
from client.file_handler import FileHandler
import os

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.txt'
        with open(self.file_path, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        os.remove(self.file_path)

    def test_read_file(self):
        handler = FileHandler(self.file_path)
        data = handler.read_file()
        self.assertEqual(data, 'This is a test file.')

    def test_serialise_json(self):
        handler = FileHandler(self.file_path)
        data = handler.serialise('json')
        self.assertTrue(data.startswith(b'"'))

    def test_serialise_xml(self):
        handler = FileHandler(self.file_path)
        data = handler.serialise('xml')
        self.assertTrue(data.startswith(b'<root>'))

    def test_serialise_binary(self):
        handler = FileHandler(self.file_path)
        data = handler.serialise('binary')
        self.assertTrue(isinstance(data, bytes))

if __name__ == '__main__':
    unittest.main()

