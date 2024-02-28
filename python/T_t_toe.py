import random # for the AI random move to play in the board.

class Board:
    # define winning combinatons on a 5x5 grid.
    winning_combos = [
        # horixontal, vertical, and diagonal combinations.
        [0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],
        [0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24],
        [0,6,12,18,24],[4,8,12,16,20]
    ]
    board = ["--"] * 25 # initialize the board with empty positions.

    # display the currnt state of the board.
    def display(self):
        print(self.board[0], self.board[1], self.board[2],self.board[3], self.board[4])
        print(self.board[5],self.board[6], self.board[7], self.board[8], self.board[9])
        print(self.board[10], self.board[11], self.board[12], self.board[13], self.board[14])
        print(self.board[15], self.board[16], self.board[17], self.board[18], self.board[19])
        print( self.board[20], self.board[21], self.board[22], self.board[23], self.board[24])
    # checking if a player has won the game.
    def winner(self, player):
        for combo in self.winning_combos:
            if self.board[combo[0]] == player and self.board[combo[1]] == player and self.board[combo[2]] == player and self.board[combo[3]] == player and self.board[combo[4]] == player:
                return True
        return False

    
    # handelling adding player movement. 
    def add(self, move, player):
        if self.board[move-1] == "--":
            self.board[move-1] = player
            return True
        else:
            return False

class Game:
    # game class to handle the gameplay.

    def __init__(self, board):
        self.board = board
        self.reset_game()

     # game start and resetting 
    def reset_game(self):
       # MG is my initials (Mohamed Gabir)and AI is the computer initials.
        self.turns = ["MG","AI", "MG", "AI","MG", "AI","MG", "AI", "MG", "AI","MG", "AI","MG",
                       "AI","MG", "AI","MG", "AI","MG", "AI", "MG", "AI","MG", "AI","MG"]
        self.board.board = ["--"] * 25


    # switching between the player MG and the AI if any used the position already taken, (do the validation) while loop.
    # also if name or AI entered a wrong value which is not from 1 - 25 
    # it should show the message then diplay the game agian(restart)
   
    def take_turn(self, player):
        move_made = False
        while not move_made:
            print("It's player " + player + "'s turn")
            if player == "AI":
                move = random.randint(1, 25)
            else:
                try:
                    move = int(input("Enter move index (1-25): "))
                    if move < 1 or move > 25:
                        raise ValueError
                except ValueError:
                    print("Invalid move, try again 1-25")
                    return False
            move_made = self.board.add(move, player)
            if not move_made:
              print("Position already taken, try again different position.")
    def play(self):
        player = self.turns.pop()
        self.board.display()
        self.take_turn(player)
    def ended(self):
        return len(self.turns) == 0
    
#main function to start and manage the game.
# endding the game and winning statues also restarting the game optioal 
# if you want to play agaim it will take back to start the game 
# if not if will show you a message about the game over 
def main():

    board = Board()
    game = Game(board)
    
    while not game.ended():
        game.play()
        if board.winner("MG"):
            board.display()
            print("Player Mohamed Gabir is the winner")
            break
        if board.winner("AI"):
            board.display()
            print("The Computer is the winner")
            break
        # Check if the game ended without a winner.
    if not (board.winner("MG") or board.winner("AI")):
        board.display()
        print("It's a Tie!")
    # handling the game restart logic.
    restrat = input("Do you want to play agin?(yes/no): ").lower()
    if restrat == "yes":
        main()
    else:
        print("Game Over. Thank You For Playing!")


# enry point of the program.
if __name__ == "__main__":
    main()
