import unittest
from unittest.mock import patch
from io import StringIO
import Advisor

class TestAdvisor(unittest.TestCase):

    def setUp(self):
        self.advisor = Advisor("TestAdvisor")

    def test_print_student_list(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.advisor.print_student_list()
            output = mock_stdout.getvalue().strip()
            self.assertIn("BisonAdvisor: Student List:", output)

    def test_print_calendar(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.advisor.print_calendar()
            output = mock_stdout.getvalue().strip()
            self.assertIn("BisonAdvisor: Calendar will be printed here.", output)

    def test_send_message_to_students(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.advisor.send_message_to_students("Test message")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BisonAdvisor: Message sent to all students: Test message", output)



if __name__ == '__main__':
    unittest.main()
