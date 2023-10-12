personal_data = "Mr. John May, born on 1998-02-16"
print(f"Description: {personal_data}")
print("Name:", personal_data[4:8])
print("Surname:", personal_data[9:12])
initials = personal_data[4] + personal_data[9]
print("Initials:", initials)
print("Born:", personal_data[-11::])