# Student Performance Analyzer
# Language: Python 3
# Libraries: Pandas, NumPy, Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

SUBJECTS = ["Maths", "Physics", "Chemistry"]   # subjects in the CSV file
MAX_MARKS = 100                                # each subject is out of 100


def get_grade(percentage):
    """Return the grade for a given percentage."""
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def load_data(filename):
    """Read the CSV file, skip rows with wrong marks, and calculate
    total, percentage and grade for every student."""
    try:
        raw = pd.read_csv(filename)
    except FileNotFoundError:
        print("File not found:", filename)
        return None

    good_rows = []                       # rows with valid marks go here

    for index, row in raw.iterrows():
        valid = True
        marks = {}
        for subject in SUBJECTS:
            value = row[subject]
            try:
                number = float(value)    # 'abc' will fail here
                if number < 0 or number > MAX_MARKS:
                    raise ValueError     # marks must be between 0 and 100
                marks[subject] = number
            except ValueError:
                print(f"Invalid marks for {row['Name']} in {subject}: '{value}'. Row skipped.")
                valid = False
                break
        if valid:
            marks["Name"] = row["Name"]
            good_rows.append(marks)

    if len(good_rows) == 0:
        print("No valid student data found.")
        return None

    df = pd.DataFrame(good_rows)
    df["Total"] = df[SUBJECTS].sum(axis=1)
    df["Percentage"] = df["Total"] / (MAX_MARKS * len(SUBJECTS)) * 100
    df["Grade"] = df["Percentage"].apply(get_grade)
    return df


def show_result(df):
    """Menu option 1: print total, percentage and grade."""
    print("\n--- RESULT ---")
    for index, row in df.iterrows():
        print(f"{row['Name']} | {int(row['Total'])} | {row['Percentage']:.2f}% | {row['Grade']}")


def show_statistics(df):
    """Menu option 2: mean, median, std dev, topper, subject averages, charts."""
    print("\n--- STATISTICS ---")
    percentages = df["Percentage"]

    mean = np.mean(percentages)
    median = np.median(percentages)
    std = np.std(percentages)
    print(f"Mean %: {mean:.2f} | Median %: {median:.2f} | Std Dev: {std:.2f}")

    # Topper = student with the highest percentage
    top = df.loc[df["Percentage"].idxmax()]
    print(f"Topper: {top['Name']} ({top['Percentage']:.2f}%)")

    # Average marks of each subject
    averages = df[SUBJECTS].mean()
    text = ", ".join(f"{s} {averages[s]:.2f}" for s in SUBJECTS)
    print("Subject averages:", text)

    # Bar chart of subject averages
    plt.figure()
    plt.bar(SUBJECTS, averages.values, color=["blue", "green", "orange"])
    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    print("Bar chart displayed")
    plt.show()

    # Histogram of percentages
    plt.figure()
    plt.hist(percentages, bins=5, color="purple", edgecolor="black")
    plt.title("Histogram of Student Percentages")
    plt.xlabel("Percentage")
    plt.ylabel("Number of Students")
    plt.show()


def main():
    filename = input("Enter CSV file name (press Enter for students.csv): ").strip()
    if filename == "":
        filename = "students.csv"

    df = load_data(filename)
    if df is None:
        return

    while True:
        print("\n===== MENU =====")
        print("1. Result")
        print("2. Statistics")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_result(df)
        elif choice == "2":
            show_statistics(df)
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Wrong choice. Please enter 1, 2 or 3.")


main()
