import sys

print ("I was here")

# Ask people how much money they have

money = int(input ("How much money do you have?"))
money_2 = int(input ("How much money do you make every year?"))

if money < 1 or money_2 < 1:
    print ("Why are giving me false data ?")
    sys.exit(1)
total_amount = money + (money_2 * 10)
print  ("You will have", total_amount, "in 10 years.")

