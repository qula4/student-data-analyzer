import pandas as pd
import matplotlib.pyplot as plt
#Data Loading and Preprocessing 
try:
    # Reads the student data from the CSV file into a Pandas DataFrame.
    # Ensure 'students.csv' is in the same folder as this Python script.
    student_data_df = pd.read_csv('students.csv')
    print("Data loaded successfully from students.csv")
    # Calculates the average mark for each student across the specified subjects.
    # Adjusts the list of subject columns if they are different in the CSV.
    student_data_df['Average_Mark'] = student_data_df[['Math', 'Science', 'History', 'English', 'Computer']].mean(axis=1)
except FileNotFoundError:
    print("Error: 'students.csv' not found. Please make sure the CSV file is in the correct directory.")
    exit() # Exit the script if the file is not found, as can't proceed without data.
#Data Analysis for Plotting
# Selects the top 5 students based on their calculated 'Average_Mark'
top_5_students = student_data_df.nlargest(5, 'Average_Mark')
#Plotting the Data
plt.figure(figsize=(10, 6)) #it sets the figure size for better readability of the plot
plt.bar(top_5_students['Name'], top_5_students['Average_Mark'], color='green')
#Adding Plot Details (Title, Labels)
plt.title('Top 5 Overall Scorers', fontsize=16) #Title of the plot
plt.xlabel('Students',fontsize=12) #Label for the X-axis
plt.ylabel('Average Marks',fontsize=12) #Label for the Y-axis
plt.xticks(rotation=45, ha='right') #Rotates X-axis labels if names are long
plt.grid(axis='y', linestyle='--', alpha=0.7) #Adds a horizontal grid for better readability
plt.tight_layout() #Adjusts layout to prevent labels from overlapping
plt.show() #Displays the plot