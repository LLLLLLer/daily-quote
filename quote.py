import random
with open('quotes.txt') as f:
    quotes = f.readlines()
print(random.choice(quotes).strip())
