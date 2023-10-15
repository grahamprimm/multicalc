import unittest
from main import MultiCalc

class TestMultiCalc(unittest.TestCase):  # Update the class name
    
    def test_interface_simplicity(self):
        app = MultiCalc()
        self.assertLessEqual(app.get_widget_count(), 10)

    def test_functionality(self):
        app = MultiCalc()
        temp_result = app.calculate_temperature(0)
        self.assertEqual(temp_result, "32.0 Fahrenheit")

    def test_error_handling(self):
        app = MultiCalc()
        error_message = app.calculate_temperature('invalid_input')
        self.assertEqual(error_message, "Invalid input")

if __name__ == "__main__":
    unittest.main()
