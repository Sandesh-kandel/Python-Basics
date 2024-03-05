import sys

# Define the three subject names
subjects = ["Science", "Social", "Maths"]

# Create an empty list to store student information
students = []

# Loop to collect data for 5 students
for _ in range(5):  # Use an underscore for the unused loop variable
    # Get student name from the user
    name = input("Enter the name of a student: ")

    # Create an empty list to store the student's marks in each subject
    marks = []

    # Loop through each subject
    for subject in subjects:
        # Continuously ask for marks until valid input is received
        while True:
            # Get marks for the current subject
            mark = int(input(f"Enter marks in {subject}: "))

            # Validate the marks (should be less than or equal to 100)
            if mark <= 100:
                # If valid, add the marks to the student's list and break the loop
                marks.append(mark)
                break
            else:
                # If invalid, print an error message and continue looping
                print("Marks should be below or equal to 100.")

    # Calculate the total marks for the student
    total_marks = sum(marks)

    # Find the highest mark the student got in any subject
    highest_mark = max(marks)

    # Calculate the student's percentage (multiply by 100 for clarity)
    percentage = (total_marks / (len(subjects) * 100)) * 100

    # Create a tuple containing student information (name, highest mark, percentage, and marks)
    student_info = (name, highest_mark, percentage, marks)

    # Add the student's information to the main list
    students.append(student_info)

# Sort the list of students by their percentage in descending order
students.sort(key=lambda s: s[2], reverse=True)

# Print a header message for the top 3 students
print("\nTop 3 students with their percentages are given in output.txt file. Please check that out.")

# Loop through the top 3 students (using slicing and starting index)
for i, (name, highest_mark, percentage, marks) in enumerate(students[:3], start=1):
    # Use a dictionary to get the appropriate ordinal suffix (st, nd, rd, th)
    ordinal_suffix = {1: "st", 2: "nd", 3: "rd"}.get(i, "th")

    # Print the student's rank, name, highest mark, and percentage
    file = open('output.txt', 'a')
    sys.stdout = file
    print(f"\n{i}{ordinal_suffix} position: {name}")
    print(f"  Highest mark: {highest_mark}")
    print(f"  Percentage: {percentage:.2f}%")
    print(f"Marks in alll these subjects: {subjects}: {marks} ")
    file.close()
