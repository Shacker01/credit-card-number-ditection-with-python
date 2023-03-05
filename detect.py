import re

credit_cards = [
    "1234-5678-90123-3456",
    "1234567890123456",
    "1234 5678 9012 3456",
    "1234-5678-9012",
    "1234-5678-9012-345678",
    "1234-5678-901-3456",

]
#Regular expression pattern for credit card numbers

pattern = r"\b(?:\d*[ -]*?){13,16}\b"

#Iterate over the credit card numbers and check if they match the pattern
# card = input("Input you credit card number: ")
for card in credit_cards:
    match = re.search(pattern, card)
    if match:
        print(f"Found credit card number: {match.group(0)}")
    else:
        print("No credit card number found.")