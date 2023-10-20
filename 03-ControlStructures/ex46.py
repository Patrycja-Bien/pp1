for i in range(0,7):
    for j in range(1,44,7):
        if i+j == 8 or i+j == 9:
            print(f"  {i+j}", end = "")
        else:
            print(f" {i+j}", end="")
    print()