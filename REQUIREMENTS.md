# Software Requirements Specification: Clearance Module

## 1. User Requirements
- UR-01: As a student, I want to check my clearance status so that I know if I am eligible for enrollment.
- UR-02: As a librarian, I want to flag a student record so that pending book fees halt their enrollment.

## 2. System Requirements (Functional)
- SR-01: The system shall query the 'Library' and 'Laboratory' database flags for the provided Student ID.
- SR-02: The system shall return a boolean 'False' for enrollment eligibility if any flag is active.

## 3. System Requirements (Non-Functional)
- NFR-01: The clearance query must resolve and return a status in under 2.0 seconds.