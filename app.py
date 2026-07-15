"""
Student Grade Calculator
-------------------------
A simple Streamlit app that takes a student's name and marks in 5 subjects,
then calculates total, percentage, grade, and pass/fail status.

Author: Tanvi Rao
"""

import streamlit as st

# ---------------------------------------------------------
# STEP 1: Basic app configuration
# ---------------------------------------------------------
st.set_page_config(page_title="Student Grade Calculator", page_icon="📘")

st.title("📘 Student Grade Calculator")
st.write("Enter the student's name and marks for 5 subjects to get the total, percentage, grade, and result.")


# ---------------------------------------------------------
# STEP 2: Function definitions
# Each function does ONE clear job. This makes the code
# easy to read, test, and reuse.
# ---------------------------------------------------------

def calculate_total(marks_list):
    """Add up marks from all subjects and return the total."""
    return sum(marks_list)


def calculate_percentage(total, max_total):
    """Convert total marks into a percentage."""
    percentage = (total / max_total) * 100
    return percentage


def get_grade(percentage):
    """
    Decide the grade based on percentage.
    Grading scale (you can change these cutoffs if your college uses different ones):
        90 and above -> A+
        80 to 89.99   -> A
        70 to 79.99   -> B
        60 to 69.99   -> C
        40 to 59.99   -> D
        below 40      -> Fail
    """
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


def get_result(percentage, marks_list, passing_marks_per_subject=33):
    """
    Decide Pass or Fail.
    Rule used here (common in many Indian universities):
      - Overall percentage must be at least 40%
      - AND the student must score at least 33 in EVERY individual subject
    Change these numbers if your institution uses a different rule.
    """
    if percentage < 40:
        return "Fail"

    for marks in marks_list:
        if marks < passing_marks_per_subject:
            return "Fail"

    return "Pass"


# ---------------------------------------------------------
# STEP 3: Collect input from the user
# ---------------------------------------------------------

st.subheader("Student Details")

name = st.text_input("Enter Student Name")

st.subheader("Enter Marks (out of 100 for each subject)")

subject1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100, step=1)
subject2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100, step=1)
subject3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100, step=1)
subject4 = st.number_input("Subject 4 Marks", min_value=0, max_value=100, step=1)
subject5 = st.number_input("Subject 5 Marks", min_value=0, max_value=100, step=1)

# Put all subject marks in one list so functions can work on them easily
marks_list = [subject1, subject2, subject3, subject4, subject5]
max_total = 500  # 5 subjects x 100 marks each


# ---------------------------------------------------------
# STEP 4: Calculate and display results when button is clicked
# ---------------------------------------------------------

if st.button("Calculate Result"):

    # Basic validation: make sure name is entered
    if name.strip() == "":
        st.error("Please enter the student's name before calculating.")
    else:
        total = calculate_total(marks_list)
        percentage = calculate_percentage(total, max_total)
        grade = get_grade(percentage)
        result = get_result(percentage, marks_list)

        st.subheader("Result")
        st.write(f"**Student Name:** {name}")
        st.write(f"**Total Marks:** {total} / {max_total}")
        st.write(f"**Percentage:** {percentage:.2f}%")
        st.write(f"**Grade:** {grade}")

        if result == "Pass":
            st.success(f"**Status:** {result} ✅")
        else:
            st.error(f"**Status:** {result} ❌")
            