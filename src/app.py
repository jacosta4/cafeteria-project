import pyinputplus as pyip

print("\n--- Welcome to the cafeteria  ---\n")

print("Please, type your frecuent customer info.\n")


first = pyip.inputStr("First Name: ")
last = pyip.inputStr("Last Name: ")
age = pyip.inputNum('Age: ')

print(f"\nHello {first.capitalize()}, welcome to our comunnity!\n")

product = pyip.inputMenu(['latte', 'americano', 'cappuccino', 'juice'], lettered=False, numbered=True )

print(f'Thank you for your order {first.capitalize()}, you can pick it up in a few minutes.')
