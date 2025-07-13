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
# Defines the subject to be analyzed for marks.
# This value should exactly match a column header in the 'students.csv' file (e.g., 'Math', 'Science', 'History').
subject_to_analyze = 'Math' #Can change this to any subject column name from the CSV.
# Preparing data for plotting; extracted student names and marks for the selected subject.
students_names = student_data_df['Name']
marks_for_subject = student_data_df[subject_to_analyze]
# Creating the bar plot.
plt.figure(figsize=(10, 6)) 
plt.bar(students_names, marks_for_subject, color='purple')
plt.title(f'Marks Analysis: {subject_to_analyze} Marks', fontsize=16)
plt.xlabel('Students', fontsize=12)
plt.ylabel(f'{subject_to_analyze} Marks', fontsize=12)
plt.xticks(rotation=45, ha='right') # Rotates X-axis labels for long student names.
plt.grid(axis='y', linestyle='--', alpha=0.7) # Adds a horizontal grid for visual guidance.
plt.tight_layout() # Adjusts layout to prevent labels from overlapping.
plt.show()