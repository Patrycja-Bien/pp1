def display_countries(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                print(f"{line_num}. {line.strip()}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

file_path = 'countries.txt'
display_countries(file_path)
