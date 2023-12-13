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



if __name__ == '__main__':
    unittest.main()
