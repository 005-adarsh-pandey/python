# Read the student data from a file
with open('students.txt', 'r') as file:
    students = file.readlines()

# Process and sort students by scores in descending order
students = [line.strip().split(': ') for line in students]  # Split into name and score
students = [(name, int(score)) for name, score in students]  # Convert score to integer
students.sort(key=lambda x: x[1], reverse=True)  # Sort by score (descending)

# Function to assign grades based on rank
def assign_grade(rank, total_students):
    percentile = rank / total_students
    if percentile <= 0.10:
        return 'S'
    elif percentile <= 0.30:
        return 'A'
    elif percentile <= 0.60:
        return 'B'
    else:
        return 'C'

# Assign grades to each student
graded_students = []
rank = 1
total_students = len(students)
for name, score in students:
    grade = assign_grade(rank, total_students)
    graded_students.append((name, score, grade))
    rank += 1

# Filter students with grades 'S' or 'A'
top_stud = filter(lambda student: student[2] in ['S', 'A'], graded_students)

# Save the filtered students to a new file
with open('top_students.txt', 'w') as file:
    for name, score, grade in top_stud:
        file.write(f"{name}: {score}: {grade}\n")
