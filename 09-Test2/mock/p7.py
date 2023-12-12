def f(arr):
    import re
    pattern = re.compile(r'^[a-z0-9_]{4,12}$')
    valid_usernames = []
    for username in arr:
        username = str(username)
        x = re.findall(pattern,username)
        if x == []:
            continue
        else:
            valid_usernames.append(x)
    return len(valid_usernames)
if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))