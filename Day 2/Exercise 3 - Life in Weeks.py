# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lata = 90 - int(age)
months = round(lata * 12)
weeks = round(lata * 52)
days = round(lata * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
