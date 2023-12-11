class Advisor:
    def __init__(self, name):
        self.name = name
        self.student_list = ['Tyson', 'Morgan', 'Maya']

    def print_student_list(self):
        if not self.student_list:
            print('*****************************')
            print("BisonAdvisor: No students in the advisor's list.")
            print('*****************************')
            print()
        else:
            print('*****************************')
            print("BisonAdvisor: Student List:")
            for student in self.student_list:
                print(student)
            print('*****************************')
            print()

    def print_calendar(self):
        # Implement the calendar printing logic here
        print('*****************************')
        print("BisonAdvisor: Calendar will be printed here.")
        print('*****************************')
        print()

    def send_message_to_students(self, message):
        print('*****************************')
        print(f"BisonAdvisor: Message sent to all students: {message}")
        print('*****************************')
        print()


def main():
    advisor_name = input("Enter your name, advisor: ")
    advisor = Advisor(advisor_name)

    def Advisor_options():
        # Advisor-specific functionality
        print("\nAdvisor Options:")
        print("1. Print Student List")
        print("2. Print Calendar")
        print("3. Send Message to Students")
        print("4. Exit")
        print()

        option = input("BisonAdvisor: Enter your choice (1-4): ")

        if option == "1":
            advisor.print_student_list()
            print('BisonAdvisor: Would you like to do anything else today?')
            Advisor_options()
        elif option == "2":
            advisor.print_calendar()
            print('BisonAdvisor: Would you like to do anything else today?')
            Advisor_options()
        elif option == "3":
            message = input("BisonAdvisor: Enter the message to send to students: ")
            advisor.send_message_to_students(message)
            print('BisonAdvisor: Would you like to do anything else today?')
            Advisor_options()
        elif option == "4":
            print("BisonAdvisor: Exiting advisor portal. Goodbye!")
        else:
            print("BisonAdvisor: Invalid input. Please enter a number between 1 and 4.")
            Advisor_options()
            print()
    Advisor_options()


if __name__ == "__main__":
    main()
