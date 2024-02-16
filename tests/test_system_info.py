import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch
from functions.system_info import get_system_version, get_cpu_info, get_memory_info, get_host_name

class TestSystemInfo(unittest.TestCase):
    @patch('platform.platform')
    def test_get_system_version(self, mock_platform):
        mock_platform.return_value = "Windows-10"
        result = get_system_version()
        self.assertIn("Wersja systemu:", result)
        self.assertIn("Windows-10", result)

        mock_platform.return_value = ""
        result = get_system_version()
        self.assertIn("Wersja systemu:", result)
        self.assertIn("", result)

    @patch('psutil.cpu_count')
    def test_get_cpu_info(self, mock_cpu_count):
        mock_cpu_count.return_value = 4
        result = get_cpu_info()
        self.assertEqual("Liczba rdzeni: 4", result)

        mock_cpu_count.return_value = None
        result = get_cpu_info()
        self.assertNotIn("Liczba rdzeni:", result)

    @patch('psutil.virtual_memory')
    def test_get_memory_info(self, mock_virtual_memory):
        mock_virtual_memory.return_value.total = 8 * (1024 ** 3)  # 8 GB
        result = get_memory_info()
        self.assertIn("RAM:", result)
        self.assertIn("8.00 GB", result)

        mock_virtual_memory.return_value.total = 0
        result = get_memory_info()
        self.assertIn("RAM:", result)
        self.assertIn("0.00 GB", result)

    @patch('socket.gethostname')
    @patch('platform.node')
    def test_get_host_name(self, mock_node, mock_gethostname):
        mock_node.return_value = "test-host"
        mock_gethostname.return_value = "test-host"
        result = get_host_name()
        self.assertEqual("Host name: test-host", result)

        mock_node.return_value = ""
        result = get_host_name()
        self.assertEqual("Host name: ", result)

if __name__ == '__main__':
    unittest.main()
