import Advisor
import Student



def main():
    print("BisonAdvisor: Welcome to the University Portal! Interact with me, the Bison Chatbox, to navigate!")

    # Ask the user if they are a student or an advisor
    user_type = input("BisonAdvisor: Are you a student or an advisor? ").lower()

    # Check the user's input and provide a response
    if user_type == "student":
        print("BisonAdvisor: Welcome, student! You can access your student portal.")
        print('****************')
        print()
        Student.main()
    elif user_type == "advisor":
        print("BisonAdvisor: Hello, advisor! You have access to the advisor portal.")
        print('****************')
        print()
        Advisor.main()
    else:
        print("BisonAdvisor: Invalid input. Please enter 'student' or 'advisor'. Restarting:")
        print()
        main()


if __name__ == "__main__":
    main()
