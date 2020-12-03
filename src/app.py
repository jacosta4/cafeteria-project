import pyinputplus as pyip

print("\n--- Welcome to the cafeteria  ---\n")

print("Please, type your frecuent customer info.\n")

first = pyip.inputStr("First Name: ")
last = pyip.inputStr("Last Name: ")
age = pyip.inputNum('Age: ')
usuario = input('Username: ')

print(f"\nHello {first.capitalize()}, welcome to our comunnity!\n")

# Productos
espre1 = 'latte'
espre2 = 'americano'
espre3 = 'cappuccino'
espre4 = 'juice'

bak1 = 'Bagel'
bak2 = 'Muffins'
bak3 = 'Biscotto'
bak4 = 'Croissant'

while True:
    count = 0
    product = pyip.inputMenu([espre1, espre2, espre3, espre4], lettered=False, numbered=True )
    print(f'Do you want to add some dessert?')
    add_postries = pyip.inputYesNo()
    if add_postries == 'yes':
        bakery = pyip.inputMenu([bak1, bak2, bak3, bak4], lettered=False, numbered=True )
        print('\nIs your order complete?')
        full_order = pyip.inputYesNo()
        if full_order == 'yes':
            break
        else:
            continue
    else:
        break

# Precios de productos y contador de factura final

if product == espre1:
    # count += 2.50
    count += 1
elif product == espre2:
    # count += 1.15
    count += 1
elif product == espre3:
    # count += 3.00
    count += 1
elif product == espre4:
    # count += 2.50
    count += 1

if bakery == bak1:
    # count += 3.25
    count += 1
elif bakery == bak2:
    # count += 2.50
    count += 1
elif bakery == bak3:
    # count += 1.75
    count += 1
elif bakery == bak4:
    # count += 4.25
    count += 1

print(f'\nYour total bill: ${count}')

print(f'\nThank you for your order {first.capitalize()}, you can pick it up your order in a few minutes.')
