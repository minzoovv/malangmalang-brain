from sys import stdin, stdout
read = lambda: stdin.readline().split()

# setup
BUTTONS = [[0, 1, 2],
           [3, 7, 9, 11],
           [4, 10, 14, 15],
           [0, 4, 5, 6, 7],
           [6, 7, 8, 10, 12],
           [0, 2, 14, 15],
           [3, 14, 15],
           [4, 5, 7, 14, 15],
           [1, 2, 3, 4, 5],
           [3, 4, 5, 9, 13]]


def exec_switch(buttons, clocks, number, press):
    # end case 
    if number > 9:
        return 31

    if all(clock % 12 == 0 for clock in clocks):
        return press

    else:
        presses = []
        for i in range(4):
            presses.append(exec_switch(buttons, clocks, number+1, press+i))
            for j in buttons[number]:
                clocks[j] += 3

        press = min(presses)
        return press


# execute
N = int(input())

for _ in range(N): 
    clocks = list(map(int, read()))
    best_press = exec_switch(BUTTONS, clocks, 0, 0)
    print(-1 if best_press == 31 else best_press)
