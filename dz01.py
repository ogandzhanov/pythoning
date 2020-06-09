# This is 1st homework of the Phyton course from http://dswz.ru
# Using "input", "print", "if" and "while"
#
i = 1
while i	>= 1:
    print("\nИтерация", i, ". Скажите, кто вы?")
    s = input("Введите Д для девочки, М для мальчика или В для выхода:")  
    if s == "Д":
        print(s, " Девочка --> Рад приветствовать прекрасную даму!", end="\n")
    elif s == "М":
        print(s, " Мальчик --> Вечер в хату, братишка, давно ли откинулся?!", end="\n")
    elif s == "В":
        break
    else:
        print(s, " [?] --> Добрый день!", end="\n")
    i += 1
print("\nДо свидания!")