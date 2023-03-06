def calculator():
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))
    operation = input("Wybierz operacje:\n""1 żeby dodać\n""2 żeby odjąć \n""3 żeby pomnożyć \n""4 żeby podzielić \n")

    if operation == '1':
        print(num1 + num2)
    elif operation == '2':
        print(num1 - num2)
    elif operation == '3':
        print(num1 * num2)
    elif operation == '4':
        print(num1 / num2)
    else:
        print("Nieprawidłowa operacja")
calculator()