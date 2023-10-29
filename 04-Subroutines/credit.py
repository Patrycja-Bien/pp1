def f(card_number):
    card_number = str(card_number)
    front = card_number[0:2]
    end = card_number[-4::]
    result = front + "**********" + end
    return result
