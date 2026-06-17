# Software Requirements Specification: Clearance Module

## 1. User Requirements
- UR-01: As a student, I want to check my clearance status so that I know if I am eligible for enrollment.
- UR-02: As a librarian, I want to flag a student record so that pending book fees halt their enrollment.

## 2. System Requirements (Functional)
- SR-01: The system shall query the 'Library' and 'Laboratory' database flags for the provided Student ID.
- SR-02: The system shall return a boolean 'False' for enrollment eligibility if any flag is active.

## 3. System Requirements (Non-Functional)
- NFR-01: The clearance query must resolve and return a status in under 2.0 seconds.
python3 -m venv .venv
source .venv/bin/activate
pip install behave
Feature: Student Enrollment Clearance

Scenario: Student has pending library fees
  Given a student with ID "A20241001" exists
  And the student has a pending "Library" fee of 500 pesos
  When the enrollment clearance system checks the student
  Then the clearance status should be "Rejected"
  And the reason should include "Library"

Scenario: Student has no pending liabilities
  Given a student with ID "A20241002" exists
  And the student has no pending liabilities
  When the enrollment clearance system checks the student
  Then the clearance status should be "Approved"

from behave import given, when, then

# Mock database
mock_database = {}
current_student_id = None
clearance_result = None

@given('a student with ID "{student_id}" exists')
def step_impl(context, student_id):
    global current_student_id
    current_student_id = student_id
    mock_database[student_id] = {"liabilities": []}

@given('the student has a pending "{dept}" fee of {amount} pesos')
def step_impl(context, dept, amount):
    mock_database[current_student_id]["liabilities"].append(dept)

@given('the student has no pending liabilities')
def step_impl(context):
    mock_database[current_student_id]["liabilities"] = []

@when('the enrollment clearance system checks the student')
def step_impl(context):
    global clearance_result
    liabilities = mock_database[current_student_id]["liabilities"]
    if len(liabilities) > 0:
        clearance_result = {"status": "Rejected", "reason": liabilities}
    else:
        clearance_result = {"status": "Approved", "reason": []}

@then('the clearance status should be "{expected_status}"')
def step_impl(context, expected_status):
    assert clearance_result["status"] == expected_status

@then('the reason should include "{expected_reason}"')
def step_impl(context, expected_reason):
    assert expected_reason in clearance_result["reason"]