
import json
file = open("students.json")
data = json.load(file)
total_age_male = 0
total_grade_male = 0
total_age_female = 0
total_grade_female = 0
gender_male = 0
gender_female = 0
for student in data["Students"]:
    if student["Gender"] == "Male":
        gender_male += 1
    elif student["Gender"] == "Female":
        gender_female += 1
for student in data["Students"]:
    if (student["Gender"]) == "Male":
        total_age_male += int(student["Age"])
        total_grade_male += int(student["Grade "])

    elif (student["Gender"]) == "Female":
        total_age_female += int(student["Age"])
        total_grade_female += int(student["Grade "])
        
    
print(total_grade_male/gender_male)       
print(total_age_female/gender_male)
print(total_grade_male/gender_female)
print(total_age_male/gender_female)