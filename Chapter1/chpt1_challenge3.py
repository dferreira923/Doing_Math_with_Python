'''
Challenge 3

The unit conversion program we wrote in this chapter is limited to conversions between kilometers and miles.
Try extending the program to convert between units of mass (such as kilograms and pounds) and between units 
of temperature (such as Celsius and Fahrenheit).
'''

def print_menu():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Fahrenheit to Celsius")
    print("4. Celsius to Fahrenheit")
    print("5. Pounds to Kilograms")
    print("6. Kilograms to Pounds")


def km_miles():
    km = float(input("Enter distance in kilometers: "))
    miles = km / 1.609

    print("Distance in miles: {0}".format(miles))


def miles_km():
    miles = float(input("Enter distance in miles: "))
    km = miles * 1.609

    print("Distance in kilometers: {0}".format(km))


def f_cel():
    f = float(input("Enter temperature in Fahrenheit: "))
    cel = ((f - 32) * 5) / 9

    print("Temperature in Celsius: {0}".format(cel))


def cel_f():
    cel = float(input("Enter temperature in Celsius: "))
    f = (cel * 1.8) + 32

    print("Temperature in Fahrenheit: {0}".format(f))


def lbs_kg():
    lbs = float(input("Enter weight in pounds: "))
    kg = lbs / 2.2046

    print("Weight in kilograms: {0}".format(kg))


def kg_lbs():
    kg = float(input("Enter weight in kilograms: "))
    lbs = kg * 2.2046

    print("Weight in pounds: {0}".format(kg))


if __name__ == '__main__':
    print_menu()
    choice = input("Which conversion would you like to do?")
    if choice == "1":
        km_miles()

    if choice == "2":
        miles_km()

    if choice == "3":
        f_cel()

    if choice == "4":
        cel_f()

    if choice == "5":
        lbs_kg()

    if choice == "6":
        kg_lbs()
