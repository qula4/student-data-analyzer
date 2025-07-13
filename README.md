# Student Marks Data Analyzer

## Project Overview
This Python project is designed to organize, analyze, and visualize student academic performance data. Developed as part of a **Data Analysis Internship**, its goal is to demonstrate fundamental data handling, analysis, and visualization skills using Python's powerful data science libraries.

## Features
* **Data Loading:** Loads student information and marks from a 'students.csv' file.
* **Average Mark Calculation:** Computes the average mark for each student across specified subjects.
* **Top Performers Identification:** Identifies and displays the top 5 students based on their average marks.
* **Visual Representation:** Generates a clear bar chart to visually present the top academic performers.

## Technologies Used

* Python
* Pandas (https://pandas.pydata.org/) -library for data manipulation and analysis
* Matplotlib (https://matplotlib.pydata.org/) - a python 2D plotting library

## How to Run the Project (For Recruiters/Your Future Self)

### Prerequisites
Make sure you have Python 3.x installed on your system.

### Setup (Local Environment)
1. **Clone this repository:**
    ```bash
    git clone [https://github.com/qula4/student-data-analyzer.git](https://github.com/qula4/student-data-analyzer.git)
    ```

2. **Navigate into the project directory:**
    ```bash
    cd student-data-analyzer
    ```
3. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
4. **Activate the virtual environment:**
    * **On Windows (PowerShell):**
        ```bash
        . .\venv\Scripts\activate
        ```
    * **On Windows (Command Prompt):**
        ```bash
        .\venv\Scripts\activate.bat
        ```
5. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Script
  Ensure you are in the project's root directory ('student-data-analyzer') with the virtual environment activated.
You can run the different analysis scripts as follows:
1. **To analyze and display top scorers:**
    ```bash
    python top_scorers_analysis.py 
    ```
2. **To analyze subject marks:**
     ```bash
    python sub_marks_analysis.py 
    ```
3. **To calculate and display pass\fail ratio:**
  ```bash
    python pass_fail_ratio.py 
    ```
