from subprocess import getoutput as gout

clear = gout("clear")

def get_plc_inps(mat_xy):
    print('pos x to y')
    plc_xy = (int(input('x = ')), int(input('y = ')))
    sym = input('sym = ')
    while len(sym) > 1:
        print(f'This are more than 1 sym')
        sym = input('sym = ')
    while plc_xy[0] > mat_xy[0] or plc_xy[1] > mat_xy[1]:
        print(f'To big nums')
        plc_xy = (int(input('x = ')), int(input('y = ')))
    return (plc_xy, sym)


def main():
    print(clear)
    try:
        print("x to y")
        mat_xy = (int(input('x = ')), int(input('y = ')))
        matrix = [["#"]*mat_xy[0] for y in range(mat_xy[1])]
        while True: 
            plc_xy, sym = get_plc_inps(mat_xy)
            print(f'Pos = x{mat_xy[0]}*y{mat_xy[1]}\nsym = {sym}')
            matrix[plc_xy[0]-1][plc_xy[1]-1] = sym
            print(clear)
            print('\n'.join(map(str, matrix)))
    except ValueError:
        print("They need to be int's")
        exit()
    except KeyboardInterrupt:
        print("\nKey C pressed, exiting...")
        exit()

if __name__ == "__main__":
    main()
