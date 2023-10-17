import unittest
# Example functions to test compatibility
def is_device_compatible(device_type):
    supported_devices = ["Fitness Tracker", "Smartphone", "Smartwatch"]
    return device_type in supported_devices
def is_data_format_compatible(data_format):
    supported_formats = ["JSON", "XML", "CSV"]
    return data_format in supported_formats
def is_os_compatible(os_name):
    supported_os = ["iOS", "Android"]
    return os_name in supported_os
# Test case class for compatibility testing
class HealthAppCompatibilityTest(unittest.TestCase):
    def test_device_compatibility(self):
        self.assertTrue(is_device_compatible("Fitness Tracker"), "Fitness Tracker compatibility failed")
        self.assertTrue(is_device_compatible("Smartphone"), "Smartphone compatibility failed")
        self.assertTrue(is_device_compatible("Smartwatch"), "Smartwatch compatibility failed")

    def test_data_format_compatibility(self):
        self.assertTrue(is_data_format_compatible("JSON"), "JSON compatibility failed")
        self.assertTrue(is_data_format_compatible("XML"), "XML compatibility failed")
        self.assertTrue(is_data_format_compatible("CSV"), "CSV compatibility failed")
    def test_os_compatibility(self):
        self.assertTrue(is_os_compatible("iOS"), "iOS compatibility failed")
        self.assertTrue(is_os_compatible("Android"), "Android compatibility failed")
if __name__ == "__main__":
    unittest.main()