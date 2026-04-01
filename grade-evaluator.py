import csv
import sys
import os


def load_csv_data():
    filename = input( "Enter the name of the CSV file to process (e.g., grades.csv): ")

    # Exit cleanly before attempting to open a file that isn't there.
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments

    except Exception as e:
        #this will catch anything unexpected like corrupted or missing files
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

#this block will run the validation, calculate scores and GPA, determines the pass or fail, and prints the transcript
def evaluate_grades(data):
    print("\n--- Processing Grades ---")

    if not data:
        print("Error: No grade data found. The file may be empty.")
        sys.exit(1)

    # Validate scores
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"ERROR: '{item['assignment']}' has invalid score: {item['score']}")
            sys.exit(1)

    # Validate weights
    total_weight = 0
    formative_weight_total = 0
    summative_weight_total = 0

    for item in data:
        total_weight += item['weight']
        if item['group'] == 'Formative':
            formative_weight_total += item['weight']
        elif item['group'] == 'Summative':
            summative_weight_total += item['weight']

    if total_weight != 100:
        print(f"ERROR: Total weights = {total_weight}, expected 100")
        sys.exit(1)
    if formative_weight_total != 60:
        print(f"ERROR: Formative weights = {formative_weight_total}, expected 60")
        sys.exit(1)
    if summative_weight_total != 40:
        print(f"ERROR: Summative weights = {summative_weight_total}, expected 40")
        sys.exit(1)

    print("All validations passed.")

    # Calculate grades
    final_grade = 0
    formative_score = 0
    summative_score = 0

    for item in data:
        # weighted contribution of this single assignment towards the final grade
        contribution = (item['score'] / 100) * item['weight']
        final_grade += contribution
        if item['group'] == 'Formative':
            formative_score += contribution
        elif item['group'] == 'Summative':
            summative_score += contribution

    #GPA calculation
    gpa = (final_grade / 100) * 5.0
    formative_percentage = (formative_score / 60) * 100
    summative_percentage = (summative_score / 40) * 100

    # Pass/Fail checker
    passed = formative_percentage >= 50 and summative_percentage >= 50

    # Resubmission checker that flags the weight
    failed_formatives = []
    for item in data:
        if item['group'] == 'Formative' and item['score'] < 50:
            failed_formatives.append(item)

    highest_weight = 0
    for item in failed_formatives:
        if item['weight'] > highest_weight:
            highest_weight = item['weight']

    resubmit = []
    for item in failed_formatives:
        if item['weight'] == highest_weight:
            resubmit.append(item)

    # Print results
    print(f"\nFormative Score:  {formative_percentage:.2f}%")
    print(f"Summative Score:  {summative_percentage:.2f}%")
    print(f"Final Grade:      {final_grade:.2f}%")
    print(f"GPA:              {gpa:.2f} / 5.0")

    if passed:
        print("\n Academic Status: PASSED")
    else:
        print("\n Academic Status: FAILED")

    if failed_formatives:
        print("\nFailed Formative Assignments:")
        for item in failed_formatives:
            print(f"  - {item['assignment']} (Score: {item['score']}%, Weight: {item['weight']})")
        print("\nRecommended for Resubmission:")
        for item in resubmit:
            print(f"  -> {item['assignment']} (Weight: {item['weight']})")
    else:
        print("\nNo formative assignments failed.")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)
