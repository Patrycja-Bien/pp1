def f(subjects):
    subject_avg = {}
    for subject, grades in subjects.items():
        subject_avg.update({subject: sum(grades) / len(grades)})

    max_subject = max(subject_avg, key=subject_avg.get)
    
    return max_subject

if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4],"x":[1,1,1,1,1]}))