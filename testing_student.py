import unittest
from unittest.mock import patch
from io import StringIO
import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("TestStudent")

    def test_advisor_meeting(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.student.advisor_meeting()
            output = mock_stdout.getvalue().strip()

        expected_output = "*****************************\n" \
                          "BisonAdvisor: Scheduled a meeting with advisor: Noha Hazzazi\n" \
                          "*****************************\n\n" \
                          "BisonAdvisor: What else can I help you with today?"

        self.assertEqual(output, expected_output)

    def test_schedule(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.student.schedule()
            output = mock_stdout.getvalue().strip()

        expected_output = "*****************************\n" \
                          "BisonAdvisor: Class Schedule:\n" \
                          "-Math\n" \
                          "-History\n" \
                          "-Real N**** 101\n" \
                          "-Hotep 101\n" \
                          "-Swagg 404\n" \
                          "Chatbot: What else can I help you with today?"

        self.assertEqual(output, expected_output)

    def test_get_pin(self):
        with patch("builtins.input", side_effect=["yes"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                self.student.get_pin()
                output = mock_stdout.getvalue().strip()

        expected_output = "*****************************\n" \
                          "BisonAdvisor: Requesting PIN from advisor.\n" \
                          "BisonAdvisor: Request sent!\n" \
                          "BisonAdvisor: Check your email, your Advisor will contact you with your pin there!\n" \
                          "*****************************\n\n" \
                          "BisonAdvisor: What else can I help you with today?"

        self.assertEqual(output, expected_output)

    def test_get_pin_already_sent(self):
        self.student.pin_request_sent = True
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.student.get_pin()
            output = mock_stdout.getvalue().strip()

        expected_output = "*****************************\n" \
                          "BisonAdvisor: PIN request already sent. Please wait for a response.\n" \
                          "*****************************\n\n" \
                          "BisonAdvisor: What else can I help you with today?"

        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
