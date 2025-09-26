student_name = "Jahiem Foster"

current_gpa = 3.1 # Float between 1.0-4.0
study_hours = 10
social_points = 40
stress_level = 50
print("Welcome")
print(f"Student Name: {student_name}")
print(f"Current GPA: {current_gpa}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")
print("Difficulty Levels: Light, Standard, Heavy")
choice = input("Your choice:" )

# Added after first commit

light_mode = "Light: (12 credits)"
standard_mode = "Standard: (15 credits)"
heavy_mode = "Heavy: (18 credits)"

if choice == "Light":
    if current_gpa <= 2.9:
        stress_level = stress_level - 20
        study_hours = study_hours + 0
        social_points = social_points + 30
    print("Light mode")
elif choice == "Standard":
    if current_gpa >= 3.0 and current_gpa <= 3.4:
        stress_level = stress_level + 20
        study_hours = study_hours + 10
        social_points = social_points -15
        print("Standard mode")
elif choice == "Heavy":
    if current_gpa >= 3.5 and current_gpa <= 4.5:
        stress_level = stress_level + 30
        study_hours = study_hours + 15
        social_points = social_points - 20
        print("Heavy mode")
else:
    print("Invalid Input")