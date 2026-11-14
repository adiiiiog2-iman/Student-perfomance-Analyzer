# Student Performance Analyzer

**PS No. 2** | Rungta International Skills University | B.Tech CSE (AI/ML) in association with IBM

**Submitted by:** Aditya Verma (RU-26-00251)
**Submitted to:** Mr. Priyanshu (IBM SME)

---

## About the Project

Checking the marks of many students by hand takes time and can have mistakes. This project reads student marks from a **CSV file** and analyses them automatically using **Python 3**.

It calculates the **total, percentage and grade** of every student, finds the **class statistics**, and shows the results with a **bar chart** and a **histogram**.

## Features

- Reads student data from a CSV file using **Pandas**
- Calculates **total, percentage and grade** for each student
- Finds **mean, median and standard deviation** of the percentages using **NumPy**
- Shows the **topper** and the **subject-wise average**
- Draws a **bar chart** (subject averages) and a **histogram** (percentages) with proper labels using **Matplotlib**
- Handles wrong input: invalid marks are reported and that row is skipped
- Simple menu: Result, Statistics, Exit

## Technologies Used

| Tool | Use |
|------|-----|
| Python 3 | Programming language |
| Pandas | Reading the CSV file and working with the data table |
| NumPy | Mean, median and standard deviation |
| Matplotlib | Bar chart and histogram |

## Grading Scale

Marks are out of 100 in each subject (Maths, Physics, Chemistry).

| Percentage | Grade |
|------------|-------|
| 90 and above | A |
| 75 to 89.99 | B |
| 60 to 74.99 | C |
| 40 to 59.99 | D |
| Below 40 | F |

## Files in this Repository

| File | Description |
|------|-------------|
| `student_analyzer.py` | Main Python program |
| `students.csv` | Sample data (Test Cases 1 and 4) |
| `test2_boundary.csv` | Data for Test Case 2 (boundary input) |
| `test3_invalid.csv` | Data for Test Case 3 (invalid input) |
| `TEST_CASE_*.png` | Output screenshots of the test cases |
| `Project_Presentation_PS2.pptx` | Project presentation |

## CSV File Format

The first line must be the header. Each next line is one student.

```
Name,Maths,Physics,Chemistry
Aman,80,70,90
Riya,60,65,70
Karan,40,35,50
```

## How to Run

1. Install Python 3 from [python.org](https://www.python.org/).
2. Install the libraries:
   ```
   pip install pandas numpy matplotlib
   ```
3. Keep `student_analyzer.py` and the CSV files in the same folder.
4. Run the program from the terminal:
   ```
   python student_analyzer.py
   ```
5. Type the CSV file name, or just press **Enter** to use `students.csv`.
6. Choose from the menu:
   ```
   1. Result
   2. Statistics
   3. Exit
   ```

## How the Program Works

| Function | What it does |
|----------|--------------|
| `get_grade()` | Uses if / elif to turn a percentage into grade A, B, C, D or F |
| `load_data()` | Reads the CSV with Pandas, skips rows with wrong marks, adds Total, Percentage and Grade |
| `show_result()` | Prints name, total, percentage and grade of every student |
| `show_statistics()` | Finds mean, median, standard deviation, topper and subject averages, and draws both charts |
| `main()` | Asks for the file name and runs the menu until the user chooses Exit |

## Test Cases

### Test Case 1: Normal
