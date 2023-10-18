first_person = input("Enter first person name: ")
first_person_age = input ("Enter first person age: ")
second_person = input("Enter second person name: ")
second_person_age = input("Enter second person age: ")
first_person_age = int(first_person_age)
second_person_age = int(second_person_age)

if first_person_age >= 18 and second_person_age >= 18:
    print(f"Both {first_person} and {second_person} are adults")

