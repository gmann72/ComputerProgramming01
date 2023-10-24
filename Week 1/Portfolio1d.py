# Define the no. of students for each case
students = [113, 175, 12]

# Iterate through each case
for num_students in students:
    # Calculate the no. of full groups
    full_groups = num_students // 24

    # Calculate the no. of students in the leftover group
    leftover_students = num_students % 24

    # Display the results
    print(f"For {num_students} students:")
    print(f"Number of full groups: {full_groups}")
    print(f"Number of students in the leftover group: {leftover_students}")
    print()
