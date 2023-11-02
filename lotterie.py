import random
number = random.randint(1, 36)

guessing_numbers = []
numbers = int(input("Wieviele Zahlen möchtest du eigeben? "))

for i in range(0, numbers):
    guessing_number = input('Welche Zahl (1-36) möchtest du eingeben? ')
    guessing_numbers.append(guessing_number)

#guessing_number = input("Welche Zahl (von 0-36) denkst du?")
for y in guessing_numbers:
    if number == y:
        print('Du hast richtig geraten')
    else:
        print('Du hast falsch geraten')