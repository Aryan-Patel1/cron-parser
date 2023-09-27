import unittest


from main.cron_parser import parse_cron_string

class TestParseCronString(unittest.TestCase):

    def test_valid_cron_string(self):
        # Test a valid cron string
        cron_string = "*/15 0 1,15 * 1-5 /usr/bin/find"
        parsed_result = parse_cron_string(cron_string)
        self.assertIsInstance(parsed_result, dict)
        self.assertEqual(parsed_result["minute"], [0,15,30,45])
        self.assertEqual(parsed_result["hour"], [0])
        self.assertEqual(parsed_result["day of month"], [1,15])
        self.assertEqual(parsed_result["day of week"], [1, 2, 3, 4 ,5])
        self.assertEqual(parsed_result["command"], "/usr/bin/find")

    def test_invalid_cron_string(self):
        # Test an invalid cron string
        cron_string = "0 9 * * *"  # Missing the command
        parsed_result = parse_cron_string(cron_string)
        self.assertIsInstance(parsed_result, str)
        self.assertEqual(parsed_result, "Invalid cron string format. Please provide a valid cron string.")

    def test_cron_string_with_special_characters(self):
        # Test a cron string with 'L' for the last day of the week
        cron_string = "20 8 ? * * /usr/bin/find"
        parsed_result = parse_cron_string(cron_string)
        self.assertIsInstance(parsed_result, dict)
        self.assertEqual(parsed_result["minute"], [20])
        self.assertEqual(parsed_result["hour"], [8])
        self.assertEqual(parsed_result["day of month"], [])
        self.assertEqual(parsed_result["day of week"], [0,1,2,3,4,5,6])
        self.assertEqual(parsed_result["command"], "/usr/bin/find")

if __name__ == '__main__':
    unittest.main()
