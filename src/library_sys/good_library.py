class OCPCalculator:
    def __init__(self):
        self.strategies = {
            "standard": lambda days: days * 10,
            "reference": lambda days: days * 50,
            "default": lambda days: days * 5
        }

    def calculate(self, book):
        strategy = self.strategies.get(book["type"], self.strategies["default"])
        return strategy(book["days_late"])


class ReportPrinter:
    def print_report(self, processed_data, total):
        print("--- FEU Alabang Library Report ---")
        for data in processed_data:
            print(f"Book: {data['title']} | Penalty: {data['penalty']} PHP")
        print(f"Total Due: {total} PHP")


if __name__ == "__main__":
    books = [
        {"title": "Software Engineering", "days_late": 5, "type": "standard"},
        {"title": "AI Fundamentals", "days_late": 2, "type": "reference"}
    ]

    calculator = OCPCalculator()
    printer = ReportPrinter()

    processed = []
    total = 0

    for b in books:
        penalty = calculator.calculate(b)
        processed.append({"title": b["title"], "penalty": penalty})
        total += penalty

    printer.print_report(processed, total)