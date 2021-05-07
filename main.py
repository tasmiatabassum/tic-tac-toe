#****Global Variables****

#will hold the game board data
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#whether the game is over or not
game_still_running = True

#who the winner is
winner = None

#who the current player is -- X goes first
current_player = "X"

#****FUNCTIONS****

#game of tic-tac-toe!
def play_game():

    #show the game board before any turns/moves
    display_board()

    #loop until someone wins/ties
    while game_still_running:
         #handle a player's turn
         handle_turn(current_player)

         #check if the game is over or not
         check_if_over()

         #give the other player the turn to player
         flip_player()

    #When the game is over, print who is the winner or if it is a tie
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("It's a Tie!!")

#display the game board = we define display_board
def display_board():
    print("\n")
    print(board[0]+ " | " +board[1]+ " | " +board[2] + "    1 | 2 | 3")
    print(board[3]+ " | "+board[4]+ " | " +board[5]  + "    4 | 5 | 6")
    print(board[6]+ " | "+board[7]+ " | " +board[8]  + "    7 | 8 | 9")
    print("\n")

#handle the player's move
def handle_turn(player):

    #get the position from the player
    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    #making sure that the input is valid and the spot isn't already taken
    valid = False
    while not valid:
         #making sure the input is valid
         while position not in ['1', '2', '3','4','5','6','7','8','9']:
             position = input("Please choose a position from 1-9: ")
        #get correct index in the game board
         position = int(position) - 1

        #making sure the spot isn't already taken in the board
         if board[position] == '-':
             valid = True
         else:
             print("That's not a valid move, you can't go there :( ")
    #put the move on the board
    board[position] = player

    #show updated game board
    display_board()

#check if the game is over or not --> defining check_if_over
def check_if_over():
    check_for_winner()
    check_for_tie()

#Check if someone has won or not
def check_for_winner():
    #set the global Variables
    global winner
    #check for winner anywhere on the board
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    #get the winner ---> defining the winners at diff places on the display_board
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

#Checking rows for a win ---> defining check_rows
def check_rows():
    #setting global variables
    global game_still_running
    #check whether the rows have same input/value or not and is not empty (!= "-")
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #if the rows have a match, declare the win
    if row_1 or row_2 or row_3 :
        game_still_running = False #game terminates if there is a match
    #returning the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # if not the above, return that there is no winner in the rows
    else :
        return None

#Checking columns for a win ---> defining check_columns
def check_columns():
    #setting global variables
    global game_still_running
    #check whether the rows have same input/value or not and is not empty (!= "-")
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    #if the columns have a match, declare the win
    if column_1 or column_2 or column_3 :
        game_still_running = False #game terminates if there is a match
    #returning the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # if not the above, return that there is no winner in the columns
    else :
        return None
 #Checking diagonals for a win ---> defining check_diagonals
def check_diagonals():
     #setting global variable
    global game_still_running
     #check whether the rows have same input/value or not and is not empty (!= "-")
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

     #if the diagonals have a match, declare the win
    if diagonal_1 or diagonal_2:
        game_still_running = False #game terminates if there is a match
     #returning the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
     # if not the above, return that there is no winner in the diagonals
    else :
        return None

#check if there is a tie ---> defining check_for_tie
def check_for_tie():
    #set global variables
    global game_still_running
     #if the game board is full
    if "-" not in board:
        game_still_running = False #since there is no empty space = game terminates
        return True
    else:
        return False #there is no tie

#flipping the players --> X to O and O to X ---> defining flip_player
def flip_player():
    #setting global variables
    global current_player
    #if current_player = X make it  O
    if current_player == "X":
        current_player = "O"
    #if current_player = O make it  X
    elif current_player == "O":
        current_player = "X"

#*****Start executing the game****
#play tic-tac-toe!

play_game()
