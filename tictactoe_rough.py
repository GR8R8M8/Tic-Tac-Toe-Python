def Main():
    import random
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0] ,'|', board[1] ,'|', board[2])
        print("----------")
        print(board[3] ,'|', board[4] ,'|', board[5])
        print("----------")
        print(board[6] ,'|', board[7] ,'|', board[8])
        print()

    def player():
        try:
            n = input()
            check_num(n, True)
        except ValueError:
            print("Please enter numerical values only")

    def machine():
        n = random.randint(1,9)
        check_num(n, False)


    def check_num(num, type):
        try:
            num -= 1
            if num in range(0,9):
                if board[num] == "X" or board[num] == "O":
                    if type == False:
                        machine()
                    else:
                        print("That location is already taken, try again!")
                        player()
                else:
                    if type == False:
                        board[num] = "O"
                    else:
                        board[num] = "X"
            else:
                if type == False:
                    machine()
                else:
                    print("That number is not on the board, try again")
                    player()
        except ValueError:
            print("Please enter numerical values only")

    def check_board():
        count = 0
        for a in combos:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("You Win!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("You Loose!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("Tie!")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Choose where to place your cross")
        player()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Computers turn...")
        machine()
        print()
Main()
