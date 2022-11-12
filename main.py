#print (f"NameError - {type(NameError)} ")

#print(zeus) #переменная
#print("hello")
try:
    print('start code')
    print (10/0) #ошибка
    print('NoErrors')
except NameError:
    print("we have an error")
except ZeroDivisionError:
    print("we have an error ZeroDivisionError")
print("the end")

print("========================================================================================")

try:
    print('start code')
    print (5/0) #ошибка
    print('NoErrors')
except (NameError, ZeroDivisionError) as error:
    print(error)
print("========================================================================================")
try:
    try:
        print('start code')
        print(error)  # помилка
        print('no error')
    except SyntaxError:
        print("Wrong Syntax")
except NameError as error:
    print(error)