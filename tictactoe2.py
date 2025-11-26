#tictactoe game

#loop until a situation is satisfied
    #ask the player to enter row and column
    #but X or Y into that row and column
    #display the board
    #x or y wins if same row or same coloumn is covered
    #after each turn system checks if win situation is fulfilled
    #if fulfilled game ends x or y wins

line = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]#Index 0,1,2

def display_board():
    print('-- TicTacToe --')
    print()
    print(f' {line[0][0]} | {line[0][1]} | {line[0][2]} ')
    print(f' {line[1][0]} | {line[1][1]} | {line[1][2]} ')
    print(f' {line[2][0]} | {line[2][1]} | {line[2][2]} ')
    print()

def check_if_win():
    winner = 0
    for i in line:
        if i[0] == i[1] == i[2]:
             return i[0]
        
    i = 0
    for j in range(3):
        if line[0][i] == line[1][i] == line[2][i]:
             return line[0][i]
        i+=1

    if line[0][0] == line[1][1] ==line[2][2]:
         winner = line[0][0]
         return winner

    if line[0][2] == line[1][1] ==line[2][0]:
         winner = line[0][2]
         return winner
        
def add_position(player,player_move):
    line[player_move[0]-1][player_move[1]-1] = player
    
turn_X = True
def get_position():
     while True:
        try:
            global turn_X 
            if turn_X:
                player = 'X'
                turn_X = False

            elif turn_X == False:
                player = 'O'
                turn_X = True
            position_taken = True
            while position_taken:
                player_input = (input(f'Player {player}, Enter row and column:').strip()).split(' ')
                print()
                position = []

                for i in player_input:
                    position.append(int(i))
                
                if line[position[0]-1][position[1]-1] == 'X' or line[position[0]-1][position[1]-1] == 'O':
                    print(f'Position already taken!❌\n')
                    position_taken = True 
                else:position_taken = False

            return position,player  
            break
        except ValueError:
                    print('Please enter valid row and column!⁉️\n(eg. 2 3)\n')
        except IndexError:
                    print('Please enter valid row and column!⁉️\n(eg. 2 3)\n')
    
def check_if_draw():
     if ' ' not in line[0] and ' ' not in line[1] and ' ' not in line[2] :
          return True
     else: return False

def play_game():
    winner = check_if_win()
    draw = check_if_draw()
    if winner and winner!=' ': 
        print(f'Congratulations {winner}. You won!🏆')
        return False
    elif draw:
        print(f'Draw. Try again!')
        return False
    else:        
        player_position,player = get_position()  
        add_position(player,player_position)
        display_board()
        return True

display_board()      
play = True

while play:
    play = play_game()

