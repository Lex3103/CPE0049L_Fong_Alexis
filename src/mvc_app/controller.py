from model import CourseModel
from view import ConsoleView


class AppController:
    def __init__(self):
        self.model = CourseModel()
        self.view = ConsoleView()

    def run(self):
        while True:
            # 1. Get data from Model
            courses = self.model.get_all_courses()

            # 2. Show data in View
            self.view.show_courses(courses)

            # 3. Get input from user
            user_input = self.view.get_user_input()

            if user_input == 'Q':
                break

            # 4. Process logic in Model
            success, msg = self.model.enroll_student(user_input)

            # 5. Show result in View
            self.view.show_message(msg, success)


if __name__ == "__main__":
    app = AppController()
    app.run()