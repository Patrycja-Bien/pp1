def f(player1,player2):
    one = 0
    two = 0
    digits = ["A","K","Q","J","T"]
    for i in player1:
        if i in digits:
            one += 10
        else:
            one += int(i)
    for i in player2:
        if i in digits:
            two += 10
        else:
            two += int(i)
    if one >= two:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))