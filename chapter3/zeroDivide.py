# try clause in function
# def spam(divideBy):
#     try:
#         return 42/divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1)) 

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2)) # run
    print(spam(12)) #run
    print(spam(0)) # run and get ZeroDivisionError
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.') # run and don't go back
