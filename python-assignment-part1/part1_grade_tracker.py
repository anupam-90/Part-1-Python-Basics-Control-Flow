# ==========================================
# Task 1 — Data Parsing & Profile Cleaning
# ==========================================
# 1. THE RAW DATA
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# Create empty list to store the results after cleaning
cleaned_students = []

print("--- STARTING DATA PROCESSING ---\n")

# TASK 1 & 2: LOOPING, CLEANING, AND VALIDATING
for student in raw_students:
    
    # 1. Clean the name: Remove extra spaces and fix the casing to Title Case
    clean_name = student["name"].strip().title()
    
    # 2. Convert roll number from string "101" to integer 101
    clean_roll = int(student["roll"])
    
    # 3. Convert marks_str into a list of actual numbers
    # We split by comma and space, then convert each piece to an integer
    marks_list = [int(m) for m in student["marks_str"].split(", ")]
    
    # TASK 2: Validate if the name only contains alphabetic characters
    # We use .replace(" ", "") to ignore the space between first and last names
    if clean_name.replace(" ", "").isalpha():
        validation_msg = "✓ Valid name"
    else:
        validation_msg = "✗ Invalid name"
    
    # Store this cleaned version into a temporary dictionary
    student_profile = {
        "name": clean_name,
        "roll": clean_roll,
        "marks": marks_list
    }
    
    # Add this profile to our main cleaned list
    cleaned_students.append(student_profile)

    # TASK 3: PRINT FORMATTED PROFILE CARDS
    print(validation_msg)
    print("================================")
    print(f"Student : {clean_name}")
    print(f"Roll No : {clean_roll}")
    print(f"Marks   : {marks_list}")
    print("================================\n")


# TASK 4: SPECIFIC REPORT FOR ROLL NUMBER 103
print("--- SPECIAL SEARCH: ROLL 103 ---")
for student in cleaned_students:
    if student["roll"] == 103:
        # Print the specific student's name in UPPER and lower cases
        print(f"Name in ALL CAPS: {student['name'].upper()}")
        print(f"Name in lowercase: {student['name'].lower()}")

print("\n--- PROCESSING COMPLETE ---")

# ==========================================
# Task 2 — Marks Analysis Using Loops & Conditionals
# ==========================================

# Initial Data
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print(f"--- Marks Report for {student_name} ---")

# REQUIREMENT 1: For Loop and Grading Logic
for i in range(len(subjects)):
    score = marks[i]
    subject = subjects[i]
    
    # Grading Scheme
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
        
    print(f"{subject}: {score} (Grade: {grade})")

# REQUIREMENT 2: Calculations
total_marks = sum(marks)
average_marks = round(total_marks / len(subjects), 2)

# Finding Highest and Lowest
highest_val = max(marks)
highest_idx = marks.index(highest_val)
highest_sub = subjects[highest_idx]

lowest_val = min(marks)
lowest_idx = marks.index(lowest_val)
lowest_sub = subjects[lowest_idx]

print("\n--- Summary ---")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Scoring Subject: {highest_sub} ({highest_val})")
print(f"Lowest Scoring Subject: {lowest_sub} ({lowest_val})")

# REQUIREMENT 3: While Loop for New Entry
print("\n--- Add New Subjects (Type 'done' to stop) ---")
new_count = 0

while True:
    sub_input = input("Enter subject name: ").strip()
    
    if sub_input.lower() == 'done':
        break
        
    marks_input = input(f"Enter marks for {sub_input}: ")
    
    # Check if input is a number
    if marks_input.isdigit():
        score = int(marks_input)
        
        # Check if score is in valid range
        if 0 <= score <= 100:
            subjects.append(sub_input)
            marks.append(score)
            new_count += 1
            print(f"Added {sub_input} successfully.")
        else:
            print("Warning: Marks must be between 0 and 100.")
    else:
        print("Warning: Please enter a valid number for marks.")

# Final Output after loop
new_average = round(sum(marks) / len(subjects), 2)
print(f"\nNew subjects added: {new_count}")
print(f"Updated overall average: {new_average}")


# ==========================================
# Task 3 — Class Performance Summary
# ==========================================

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# Counters for final summary
pass_count = 0
fail_count = 0
total_averages_sum = 0
topper_name = ""
topper_avg = 0

# REQUIREMENT 2: Header for the table
print(f"{'Name':<18} | {'Average':<7} | Status")
print("-" * 40)

# REQUIREMENT 1: Processing the Loop
for student in class_data:
    name = student[0]
    marks = student[1]
    
    # Calculate individual average
    avg = round(sum(marks) / len(marks), 2)
    total_averages_sum += avg
    
    # Determine Pass/Fail
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1
        
    # Check for Topper
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name
        
    # REQUIREMENT 2: Print formatted row
    # :<18 means "reserve 18 spaces and align left"
    print(f"{name:<18} | {avg:<7.2f} | {status}")

# REQUIREMENT 3: Final Summary Stats
class_avg = round(total_averages_sum / len(class_data), 2)

print("-" * 40)
print(f"Students Passed: {pass_count}")
print(f"Students Failed: {fail_count}")
print(f"Class Topper: {topper_name} ({topper_avg})")
print(f"Overall Class Average: {class_avg}")

# ==========================================
# Task 4 — String Manipulation Utility
# ==========================================

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# STEP 1: Strip leading and trailing whitespace
# This is our base version for all following steps
clean_essay = essay.strip()
print(f"Step 1 (Cleaned Essay): {clean_essay}")

# STEP 2: Convert to Title Case
title_essay = clean_essay.title()
print(f"Step 2 (Title Case): {title_essay}")

# STEP 3: Count occurrences of "python"
# Since clean_essay started as lowercase, we can count directly
python_count = clean_essay.count("python")
print(f"Step 3 (Python Count): {python_count}")

# STEP 4: Replace "python" with "Python 🐍"
emoji_essay = clean_essay.replace("python", "Python 🐍")
print(f"Step 4 (Emoji Replace): {emoji_essay}")

# STEP 5: Split into individual sentences
# We split by a period followed by a space
sentence_list = clean_essay.split(". ")
print(f"Step 5 (Sentence List): {sentence_list}")

# STEP 6: Print numbered sentences
print("Step 6 (Numbered Sentences):")
for i in range(len(sentence_list)):
    sentence = sentence_list[i].strip()
    
    # Add a period if it's missing (Requirement 6)
    if not sentence.endswith("."):
        sentence += "."
        
    # Numbering starts from 1, so we use i + 1
    print(f"{i + 1}. {sentence}")
