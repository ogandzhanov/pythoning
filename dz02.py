# This is 2dn homework of the Phyton course from http://dswz.ru
# Using "try" and "for" 
# 
# Спросим число
s = None
s = input("Введите число, для которого надо вычислить факториал:")
try:
  n = int(s)
except ValueError:
  print('Это не число. Выходим.')
except Exception:
  print('Это что ещё такое?')
else:
  #Вычислим факториал
  f = 1
  for i in range(1,n+1):
    f = f*i
  print("факториал от числа", n,"=", f)
finally:
  print("До свидания!")
# Именно в таком порядке: try, группа except, затем else, и только потом finally.