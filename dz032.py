# This is 3rd homework of the Phyton course from http://dswz.ru
# Using functions (this is main file)
# 
from dz031 import my_age as my_fun
s = input("Введите свой возраст:")
try:
  n = int(s)
except ValueError:
  print('Это не число, так не бывает.')
except Exception:
  print('Это что ещё такое?')
else:
  # Вызовем функцию
  f = my_fun(n)
  print("В", n, "лет вам {}.".format(f))
finally:
  print("До свидания!")