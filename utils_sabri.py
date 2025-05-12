
"""
File: utils_sabri.py
Author: Sabri Hamdaoui
Description: This module prints a professional byline and performs basic statistics for Sabri Insights.
"""

import statistics

# Company Information
company_name = "Sabri Insights"
tagline = "Turning Data into Value"
has_international_clients = True
years_in_operation = 5
skills_offered = ["Python", "Data Cleaning", "Power BI"]
client_satisfaction_scores = [4.9, 4.8, 5.0, 4.7, 4.6]

# Function to return company byline
def get_byline():
    return f"{company_name}: {tagline}"

# Function to count the number of offered skills
def count_skills():
    return len(skills_offered)

# Function to display statistical report
def show_stats():
    print("-" * 56)
    print(get_byline())
    print("-" * 56)
    print(f"Has International Clients: {has_international_clients}")
    print(f"Years in Operation: {years_in_operation}")
    print(f"Skills Offered: {skills_offered}")
    print(f"Number of Skills Offered: {count_skills()}")
    print(f"Client Satisfaction Scores: {client_satisfaction_scores}")
    print(f"Minimum Satisfaction Score: {min(client_satisfaction_scores)}")
    print(f"Maximum Satisfaction Score: {max(client_satisfaction_scores)}")
    print(f"Mean Satisfaction Score: {statistics.mean(client_satisfaction_scores):.2f}")
    print(f"Standard Deviation of Satisfaction Scores: {statistics.stdev(client_satisfaction_scores):.2f}")

# Main function to run the program
def main() -> None:
    print("START main() in utils_sabri.py")
    show_stats()
    print("END main() in utils_sabri.py")

# Run main only if this file is executed directly
if __name__ == "__main__":
    main()