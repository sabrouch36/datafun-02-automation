"""
File: sabri_project_setup.py
Author: Sabri Hamdaoui
Description: This script automates project folder setup and practices Python fundamentals.
"""

# Step 1: import needed modules
import os
from pathlib import Path
from utils_sabri import get_byline

# Step 2: define a function with if/elif/else
def evaluate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"

# Step 3: define a function using while loop
def count_to(number):
    count = 1
    while count <= number:
        print(f" Count: {count}")
        count += 1

# Step 4: define a function to create folders
def create_project_folders():
    base_path = Path("automation_projects")
    folders = ["data", "images", "scripts", "results"]
    for folder in folders:
        path = base_path / folder
        path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created folder: {path}")

# Step 5: define the main function
def main():
    print("Running sabri_project_setup.py...")
    print(get_byline())  # Call function from Module 1
    create_project_folders()
    result = evaluate_score(82)
    print(f" Student score evaluation: {result}")
    count_to(5)

# Step 6: define a function using match-case (Python 3.10+)
def activity_by_day(day: str):
    match day.lower():
        case "monday":
            return " Start of the work week!"
        case "friday":
            return " Almost weekend!"
        case "saturday" | "sunday":
            return " Weekend vibes!"
        case _:
            return " Regular workday"
# Step 7: define a function using lambda and filter
def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# Step 8: run the script
if __name__ == "__main__":
    main()
    message = activity_by_day("Friday")
    print(f" Day message: {message}")
    evens = filter_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"🔍 Even numbers: {evens}")


