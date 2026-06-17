class CourseModel:
    def __init__(self):
        # Simulated database
        self.db = {
            "CPE0049": {"name": "Software Design", "slots": 2},
            "CPE0050": {"name": "Computer Architecture", "slots": 0}
        }

    def get_all_courses(self):
        return self.db

    def enroll_student(self, course_code):
        course = self.db.get(course_code)

        if not course:
            return False, "Course not found."

        if course["slots"] <= 0:
            return False, "Course is full."

        course["slots"] -= 1
        return True, f"Successfully enrolled in {course['name']}."