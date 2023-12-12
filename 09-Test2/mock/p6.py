def f(years, course):
    import json
    with open("data.json", "r") as file:
        json_file = json.load(file)
    
    counter = 0
    for student in json_file:
        age = 0
        if student["age"] >= years:
            age = 1
        
        for study_course in student["studies"]["courses"]:
            if course == study_course["name"]:
                arithmetic_mean = sum(study_course["grades"]) / len(study_course["grades"])
                if arithmetic_mean >= 4:
                    if age == 1:
                        counter += 1
    return counter

if __name__ == "__main__":
    print(f(21, "statistics"))