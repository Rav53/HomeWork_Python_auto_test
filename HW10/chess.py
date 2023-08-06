import chess.chess_class as ch

if __name__ == '__main__':
    games = ch.ChessGame()
    print(games.gen_true_positions(2))