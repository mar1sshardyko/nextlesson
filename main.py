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
print("==========NEXTLESSON===================")
def checking(var_1):
    if type(var_1) != str:
        raise TypeError (f"Sorry!")
    else:
        return var_1
    checking("10")
    class BuildingError(Exception)
        def __str__(self):
            return f"ТЕКСТ НЕ ПИШЕМ"
def check_material (amount_material, limit value)