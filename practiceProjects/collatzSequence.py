def collatz(number):
    while number != 1:
        print(number)
        isEven = number % 2 == 0   
        if (isEven):
            number = number // 2
        else: 
            number = 3 * number + 1
    print(number)

input = int(input('Ingrese un número porfavor: '))

collatz(input)
