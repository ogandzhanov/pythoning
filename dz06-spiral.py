# This is 6th homework of the Phyton course from http://dswz.ru
#
# Using nested list and doctest
# Example of the expected output https://sun9-67.userapi.com/7zw05GX5TnCbx4gLWoaYhB-i-KuspEKuAJotag/tdapReOdeh0.jpg

def print_board(n):
    """
    This is doctest features testing
    >>> print_board(5)
    Выводим числа от 0 до 25 из центра по часовой стрелке:
     21  22  23  24  25 
     20   7   8   9  10 
     19   6   1   2  11 
     18   5   4   3  12 
     17  16  15  14  13 

    >>> print_board(1)
    Выводим числа от 0 до 1 из центра по часовой стрелке:
      1 
    """
    if n<1:
        return
    # Создадим список списков нужного размера
    board = list()
    for i in range(n):
        bstring = list()
        for j in range(n):
            bstring.append(None)
        board.append(bstring)
    # Заполним его нужными значениями
    m = n ** 2
    dx,dy = 1,0         
    x,y = n-1,0  
    for i in range(1,n**2+1):
        board[x][y] = m
        m -= 1
        nx,ny = x-dx, y+dy # против часовой -> x,y = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and board[nx][ny] == None:
            x,y = nx,ny
        else:
            dx,dy = -dy,dx
            x,y = x-dx, y+dy # против часовой -> x,y = x+dx, y+dy
    # Выведем на экран
    print ("Выводим числа от 0 до {} из центра по часовой стрелке:".format(n**2))
    for y in range(n):
        for x in range(n):
            print (f'{board[x][y]:{3}}',end=' ')
        print()

# Спросим число
s = None
s = input("Введите количество столбцов:")
try:
  n = int(s)
except ValueError:
  print('Это не число. Выходим.')
except Exception:
  print('Это что ещё такое?')
else:
    print("Выбран размер поля {}х{}!".format(n,n))
    print_board(n)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
