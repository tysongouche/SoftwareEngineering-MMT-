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

    def chatbot_class(self):
        #import openai
        from dotenv import load_dotenv, find_dotenv   # get the system environment variables
        import sys  # get command line arguments        
        from langchain.llms import OpenAI        
        load_dotenv(find_dotenv())  # load the environment variables      
        query = sys.argv[1] # get the argument string command line   
        llm = OpenAI(model_name="text-davinci-003") #instantiate a Davinci LLM        
        result = llm(query) # execute a query from command line
        print("Query #1 (CMDLINE) *****\n" + result, end='\n')

if __name__ == "__main__":
    unittest.main()
