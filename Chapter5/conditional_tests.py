'''
car = "subaru"
print("Is car == 'subaru' ? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi' ? I predict False.")
print(car == "audi")

car = "integra"
print(car == "integra")

car = "honda"
print(car == "acura")

car = "ford"
print(car == "datsun")

car = "ford"
print(car == "ford")

car = "chevy"
print(car == "chevrolet")

car = "nissan"
print(car == "bullshit")

car = "toyota"
print(car == "toyota")

car = "bronco"
print(car == "bronco")

car = "ranger"
print(car == "ranger")
'''

string = "i like women"
print(string == "i like women")

letters = ["A", "B", "C", "D", "E"]
for letter in letters:
    print(letter.lower())

number = 7
if number == 7:
    print("Best number in the world!")
else:
    print("Wrong!")

number = 3
if number > 3:
    print("Too big")
if number < 3:
    print("Too small")
if number == 3:
    print("Just right")

age = 21
gender = "woman"
if age >= 35 and gender == "woman":
    print("You get in for free tonight!")
if age < 35 or gender != "woman":
    print("That will be $70 please.")