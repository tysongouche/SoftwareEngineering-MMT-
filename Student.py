class Student:
    def __init__(self, name):
        self.name = name
        self.class_schedule = ['Math', 'History', 'Real N**** 101', 'Hotep 101', 'Swagg 404']
        self.pin_request_sent = False

    def advisor_meeting(self):
        print('*****************************')
        print(f"BisonAdvisor: Scheduled a meeting with advisor: Noha Hazzazi")
        print('*****************************')
        print()
        print('BisonAdvisor: What else can I help you with today?')
    def schedule(self):
        print('*****************************')
        print("BisonAdvisor: Class Schedule:")
        for class_info in self.class_schedule:
            print('-'+class_info)
        print('Chatbot: What else can I help you with today?')

    def get_pin(self):
        if not self.pin_request_sent:
            print('*****************************')
            print("BisonAdvisor: Requesting PIN from advisor.")
            print('BisonAdvisor: Request sent!')
            self.pin_request_sent = True
            print('BisonAdvisor: Check your email, your Advisor will contact you with your pin there!')
            print('*****************************')
            print()
            print('BisonAdvisor: What else can I help you with today?')

        else:
            print('*****************************')
            print("BisonAdvisor: PIN request already sent. Please wait for a response.")
            print('*****************************')
            print()
            print('BisonAdvisor: What else can I help you with today?')


def main():
    student_name = input("BisonAdvisor: Enter your name or ID number: ")
    student = Student(student_name)

    def options():
        # Student-specific functionality
        print("\nStudent Options:")
        print("1. Advisor Meeting")
        print("2. Schedule")
        print("3. Get Pin")
        print("4. Exit")
        print()

        option = input("BisonAdvisor: Enter your choice (1-4): ")

        if option == "1":
            student.advisor_meeting()
            options()
        elif option == "2":
            student.schedule()
            options()
        elif option == "3":
            student.get_pin()
            options()
        elif option == "4":
            print("Exiting Student portal. Goodbye!")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
            print('Would you like to do anything else today?')
            options()
    options()


if __name__ == "__main__":
    main()
