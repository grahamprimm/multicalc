import unittest
from main import MultiCalc

class TestMultiCalc(unittest.TestCase):
    
    def test_interface_simplicity(self):
        app = MultiCalc()
        self.assertLessEqual(app.get_widget_count(), 10)

    def test_functionality_temperature(self):
        app = MultiCalc()
        temp_result = app.calculate_temperature(0)
        self.assertEqual(temp_result, "32.0 Fahrenheit")

    def test_functionality_currency(self):
        app = MultiCalc()
        result = app.calculate_currency(100, '($)', '(€)')
        self.assertEqual(result, "€ 95.0")
        result = app.calculate_currency(100, '($)', '(¥)')
        self.assertEqual(result, "¥ 732.0")
        result = app.calculate_currency(100, '(€)', '(¥)')
        self.assertEqual(result, "¥ 774.0")

    def test_functionality_slope(self):
        app = MultiCalc()
        result = app.calculate_slope([1,1], [12,15])
        self.assertEqual(result, "Slope: 1.27") 
        app = MultiCalc()
        result = app.calculate_slope([1,1], [1,2])
        self.assertEqual(result, "Undefined (vertical line)")

    def test_error_handling(self):
        app = MultiCalc()
        error_message = app.calculate_temperature('invalid_input')
        self.assertEqual(error_message, app.TempCalc_APP.ERROR_STR)
        error_message = app.calculate_currency('invalid', '($)', '($)')
        self.assertEqual(error_message, app.Currency_APP.ERROR_STR)
        error_message = app.calculate_slope('invalid', 'invalid')
        self.assertEqual(error_message, app.Slope_APP.ERROR_STR)

    def test_functionality_inches_to_feet(self):
        app = MultiCalc()
        inches = 24
        result = app.calculate_inches_to_feet(inches)
        self.assertEqual(result, "2.0 feet")

if __name__ == "__main__":
    unittest.main()
