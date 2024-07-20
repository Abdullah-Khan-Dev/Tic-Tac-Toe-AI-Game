from unitility_functions import print_board, check_winner, is_full, find_best_move


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'O'
    ai = 'X'

    while True:
        print_board(board)
        if check_winner(board) or is_full(board):
            break

        if player == 'O':
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == ' ':
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print("You win!")
                    return
                player = ai
            else:
                print("Invalid move. Try again.")
        else:
            print("AI's turn...")
            row, col = find_best_move(board)
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print("AI wins!")
                return
            player = 'O'

    if is_full(board) and not check_winner(board):
        print_board(board)
        print("It's a draw!")


if __name__ == "__main__":
    main()
