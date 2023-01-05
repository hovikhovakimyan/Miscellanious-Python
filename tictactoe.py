moves = [[0,1,2],[3,4,5],[6,7,8]]
turn = 0
def print_board():
    print("-----------")
    for row in range(0,3):
        print(f" {moves[row][0]} | {moves[row][1]} | {moves[row][2]}")
        print("-----------")
        

def select_move():
    global turn
    selection = -1
    while(not 0<=selection<=8):
        try:
            selection = int(input("Select which box: "))
        except:
            print("Invalid Input")
    if moves[selection//3][selection%3] != 'X' and moves[selection//3][selection%3] != 'O':
        moves[selection//3][selection%3] = 'X' if turn%2==0 else 'O'
        turn+=1
    else:
        print("Move has been played")
        select_move()
        
def check_for_win():
    global turn
    #check rows
    for row in range(0,3):
        if moves[row][0] == moves[row][1] == moves[row][2]:
            print_board()
            print(f"{moves[row][0]} wins")
            return True
    #check colums
    for col in range(0,3):
        if moves[0][col] == moves[1][col] == moves[2][col]:
            print_board()
            print(f"{moves[0][col]} wins")
            return True
    #check diagnols
    if(moves[0][0] == moves[1][1] == moves[2][2]):
        print_board()
        print(f"{moves[0][0]} wins")
        return True
    if(moves[0][2] == moves[1][1] == moves[2][0]):
        print_board()
        print(f"{moves[0][2]} wins")
        return True
    #check for draw
    if turn==9:
        print_board()
        print("Its a draw")
        return True
    return False

win = False
while(not win):
    print_board()
    select_move()
    win = check_for_win()
            
