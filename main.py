from game import Board

if __name__ == '__main__':
    board = Board()

    directions_dict = {
        'w': 'up',
        'a': 'left',
        's': 'down',
        'd': 'right'
    }

    print('\n',board, '\n', sep='')

    while True:
        # Get next move
        key = input("Enter move (w/a/s/d) or 'q' to quit, 'r' to restart: ").lower()
        
        if key == 'q':
            break
        elif key == 'r':
            board = Board()
            print('\n',board, '\n', sep='')
            continue
        elif key in ['w', 'a', 's', 'd']:
            key = directions_dict[key]
            board.move(key)
            print('\n',board, '\n', sep='')
            
            if board.is_game_over():
                print("Game Over!")
                if input("Play again? (y/n): ").lower() != 'y':
                    break
                board = Board()
                print('\n',board, '\n', sep='')
