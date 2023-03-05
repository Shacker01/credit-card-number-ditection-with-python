def is_credit_card_valid(card_number):
    """
        Checks if a given credit card number is a valid using the Luhn Algorithm.
    """
    #Reverse the card number and convert to list of integers
    digits = [int(d) for d in str(card_number)][::-1]

    doubled_digitis = [digits[i] * 2 if i % 2 ==1 else digits[i] for i in range(len(digit))]

    summed_digits = [sum(int(d) for d in str(doubled_digitis[i])) if doubled_digitis[i] > 9 else doubled_digitis[i] for i in range(len(doubled_digitis))]

    return sum(summed_digits) % 10 == 0

    card_number = input("Please enter your credit card number: ")

    if is_credit_card_valid(card_number):
        print("Your credit card number is valid!")
    else:
        print("Your credit card number is not valid.")