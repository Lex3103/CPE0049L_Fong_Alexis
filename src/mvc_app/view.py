class ConsoleView:
    def show_courses(self, courses):
        print("\n--- Available Courses ---")
        for code, details in courses.items():
            status = "OPEN" if details["slots"] > 0 else "FULL"
            print(f"[{code}] {details['name']} - {status}")
        print("-------------------------")

    def show_message(self, message, is_success=True):
        prefix = "[SUCCESS]" if is_success else "[ERROR]"
        print(f"{prefix} {message}")

    def get_user_input(self):
        return input("Enter Course Code to enroll (or 'Q' to quit): ").strip().upper()