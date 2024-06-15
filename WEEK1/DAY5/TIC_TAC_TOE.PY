def display_board(board):
    frame_top_bottom = '*' * 13
    print(frame_top_bottom)
    for row in [board[i:i+3] for i in range(0, len(board), 3)]:
        print('* ' + ' | '.join(row) + ' *')
        if row != board[-3:]:
            print('*---+---+---*')
    print(frame_top_bottom)

def player_input(board, player):
    while True:
        try:
            position = int(input(f"Player {player}, choose your position (1-9): ")) - 1
            if position not in range(9):
                raise ValueError
            if board[position] == ' ':
                board[position] = player
                break
            else:
                print("This position is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

def play():
    while True:
        board = [' ' for _ in range(9)]
        current_player = 'X'
        
        for _ in range(9):
            display_board(board)
            player_input(board, current_player)
            
            if check_win(board):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            display_board(board)
            print("It's a tie!")

        new_game = input("Do you want to start a new game? (yes/no): ").lower()
        if new_game != 'yes':
            print("Thanks for playing!")
            break

play()
