def f(card_number):
    card_number = str(card_number)
    start = card_number[0:2]
    end = card_number[-4::]
    return start + 10*"*" + end


if __name__ == "__main__":
    print(f("5290312400019022")) #returns "52**********9022"