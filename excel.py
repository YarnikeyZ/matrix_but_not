from subprocess import getoutput as gout

rows = []
clear = gout("clear")

def matrix(s_x, s_y):
    for n in range(1, s_x+1):
        row = []
        for n in range(1, s_y+1):
            row.append('#')
        rows.append(row)

def addsymbol(rows, x, y, s_x, s_y, symbol):
    print(clear)
    if len(symbol) > 1:
        return f'This are more than 1 symbol'
    if x > s_x or y > s_y:
        return f'To big num'
    print(f'Pos = x{x}*y{y}')
    print(f'Symbol = {symbol}')
    columns = 'x'
    for column_num in range(0, s_x):
    	columns += f' {column_num+1}   '
    columns += 'y'
    print(columns)
    for row, row_num in zip(rows, range(0, s_y)):
        if row_num == y-1:
            row[x-1] = symbol
        print(f'{row} {row_num+1}')
 
def main():
    try:
        global s_x, s_y
        print(clear)
        try:
            print("x to y")
            s_x = int(input('x = '))
            s_y = int(input('y = '))
            matrix(s_x, s_y)
        except ValueError:
                print("They need to be int's")
                main()
    except KeyboardInterrupt:
        print("Key C pressed, exiting...")
        exit()
 
if __name__ == "__main__":
    main()
 
while True: 
    try:
        print('Pos x to y')
        addsymbol(rows, int(input('x = ')), int(input('y = ')), s_x, s_y, input('symbol = '))
    except ValueError: 
        print("They need to be int's")
    except KeyboardInterrupt:
        print("Key C pressed, exiting...")
        exit()
