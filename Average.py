def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3


num_students = int(input("How many students will be processed? "))


while num_students < 3:
    print("Please enter at least 3 students.")
    num_students = int(input("How many students will be processed? "))


for student in range(1, num_students + 1):

    print("\nStudent", student)

    name = input("Enter student's name: ")

    activity1 = float(input("Enter Activity 1 score: "))
    activity2 = float(input("Enter Activity 2 score: "))
    activity3 = float(input("Enter Activity 3 score: "))

    average = calculate_average(activity1, activity2, activity3)

    if average >= 90:
        status = "Excellent"
    elif average >= 75:
        status = "Passed"
    else:
        status = "Needs Improvement"

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Activity 1:", activity1)
    print("Activity 2:", activity2)
    print("Activity 3:", activity3)
    print("Average:", round(average, 2))
    print("Status:", status)