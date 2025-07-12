import pandas as pd
import matplotlib.pyplot as plt
# Loads student data from the CSV file into a Pandas DataFrame.
# Ensures 'students.csv' is located in the same directory as this script.
try:
    student_data_df = pd.read_csv('students.csv')
    print("Data loaded successfully from students.csv")
except FileNotFoundError:
   print("Error: 'students.csv' not found. Please make sure the CSV file is in the correct directory.")
   exit() # Exits the script if the file is not found.
# Defines the passing mark threshold.
passing_mark = 65
# Calculates 'Average_Mark' for each student if not already present in the CSV.
# This assumes marks for 'Math', 'Science', 'History', 'English', 'Computer' are present.
# Adjusts the list of subjects if the CSV has different columns for marks.
if 'Average_Mark' not in student_data_df.columns:
    subject_columns = ['Math', 'Science', 'History', 'English', 'Computer'] # Customize these subjects based on CSV
    # Ensures all required subjects columns exists before calculating average
    for col in subject_columns:
        if col not in student_data_df.columns:
            print(f"Error: Subject column '{col}' not found in students.csv for average calculation.")
            exit()
    student_data_df['Average_Mark'] = student_data_df[subject_columns].mean(axis=1)
# Determines pass/fail status based on the average mark.
# Counts students whose average mark is greater than or equal to the passing mark.
passed_students_count = student_data_df[student_data_df['Average_Mark'] >= passing_mark].shape[0]
failed_students_count = student_data_df[student_data_df['Average_Mark'] < passing_mark].shape[0]
labels = ['Passed','Failed']
sizes = [passed_students_count, failed_students_count]
colors ='blue', 'red' # blue represents passed, red represents failed students.
explode = (0.1, 0) # Slightly "explode" the 'Passed' slice for emphasis.
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title(f'Pass/Fail Ratio (Passing Mark: {passing_mark})', fontsize=8)
plt.axis('equal') # pie is drawn as a circle
plt.show()