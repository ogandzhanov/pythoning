# This is 3rd homework of the Phyton course from http://dswz.ru
# Using functions (this is function's file)
# 
def my_age(age=0):
  if age < 7:
    s = "надо в детский сад"
  elif age < 16:
    s = "пора в школу"
  elif age < 21:
    s = "пора в институт"
  elif age < 65: 
    s = "пора на работу"
  else:
    s = "пора за пенсией"
  return s