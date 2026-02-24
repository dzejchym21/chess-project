import random
from engine.board import Move

# It is a function which finds the best move using greedy algorithm
def find_best_move(board):
    turn_multiplier = 1 if board.white_to_move else -1
    opponent_color = 'b' if board.white_to_move else 'w'

    all_pieces = board.white_pieces if board.white_to_move else board.black_pieces
    legal_moves_with_pieces = []

    for piece in all_pieces:
        moves = board.get_legal_moves(piece)
        for m in moves:
            legal_moves_with_pieces.append((piece, m))

    if not legal_moves_with_pieces:
        return None

    best_score = -float('inf')
    best_move = None

    random.shuffle(legal_moves_with_pieces)
    for piece, target_sq in legal_moves_with_pieces:
        from_sq = piece.pos
        move_obj = Move(from_sq, target_sq, board)

        # We start simulation using make_move(is_virtual=True)
        # AI will always choose Queen if the promotion is available
        board.make_move(move_obj, is_virtual=True, promoted_to='Queen')
        current_score = turn_multiplier * board.evaluate()

        if current_score > best_score:
            best_score = current_score
            best_move = move_obj

        board.undo_move()

    return best_move