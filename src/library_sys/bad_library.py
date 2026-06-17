class LibraryManager:
    def __init__(self):
        self.overdue_books = [
            {"title": "Software Engineering", "days_late": 5, "type": "standard"},
            {"title": "AI Fundamentals", "days_late": 2, "type": "reference"}
        ]

    def process_penalties(self):
        print("--- FEU Alabang Library Report ---")
        total_penalty = 0

        for book in self.overdue_books:
            # Calculation logic
            if book["type"] == "standard":
                penalty = book["days_late"] * 10
            elif book["type"] == "reference":
                penalty = book["days_late"] * 50
            else:
                penalty = book["days_late"] * 5

            total_penalty += penalty

            # Output logic
            print(f"Book: {book['title']} | Penalty: {penalty} PHP")

        print(f"Total Due: {total_penalty} PHP")


if __name__ == "__main__":
    app = LibraryManager()
    app.process_penalties()