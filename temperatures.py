import random


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    filename_fahrenheit = "temps_input.txt"
    filename_celsius = "temps_output.txt"
    in_file = open(filename_fahrenheit, "r")
    out_file = open(filename_celsius, "w")

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        try:
            temperatures_number = int(input("How many random temperature(s) you want add: "))
            input_file(temperatures_number)
        except ValueError:
            print("Must be valid numbers!")
        except ZeroDivisionError:
            print("Cannot be zero!")

        if choice == "C":
            for i in in_file:
                result = fahrenheit_to_celsius(float(i))
                out_file.write(f"{result}\n")
        elif choice == "F":
            for i in in_file:
                result = celsius_to_fahrenheit(float(i))
                out_file.write(f"{result}\n")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

    in_file.close()
    out_file.close()


def input_file(valid):
    filename_fahrenheit = "temps_input.txt"
    input_temperatures_file = open(filename_fahrenheit, "w")
    for i in range(valid):
        temperature = random.uniform(-200, 200)
        input_temperatures_file.write(f"{temperature}\n")
    input_temperatures_file.close()


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()