secretnumber = 8
while True:
    guess = int(input("Guess the number: "))
    if guess == secretnumber:
     print("Congratulations!")
     break
    else:
       print("Try again!")