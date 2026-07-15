# 📘 Student Grade Calculator

A simple, beginner-friendly Streamlit web app that calculates a student's
total marks, percentage, grade, and pass/fail status based on marks in 5 subjects.

## Features
- Enter student name and marks for 5 subjects (out of 100 each)
- Automatically calculates:
  - Total marks
  - Percentage
  - Grade (A+, A, B, C, D, Fail)
  - Pass / Fail status

## Grading Logic
| Percentage      | Grade |
|-----------------|-------|
| 90% and above   | A+    |
| 80% – 89.99%    | A     |
| 70% – 79.99%    | B     |
| 60% – 69.99%    | C     |
| 40% – 59.99%    | D     |
| Below 40%       | Fail  |

**Pass/Fail Rule:** Overall percentage must be at least 40%, and the student
must score at least 33 marks in every individual subject.

## How to Run Locally

1. Clone this repository:
   \`\`\`
   git clone https://github.com/tanvi-rao02/student-grade-calculator.git
   cd student-grade-calculator
   \`\`\`

2. Create a virtual environment:
   \`\`\`
   python -m venv venv
   venv\\Scripts\\activate
   \`\`\`

3. Install dependencies:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

4. Run the app:
   \`\`\`
   streamlit run app.py
   \`\`\`

## Tech Stack
- Python
- Streamlit

## Live Demo
_Add your Streamlit Cloud link here after deployment._

## Author
Tanvi Rao
