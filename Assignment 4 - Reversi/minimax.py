INFINITY = 100000


class Minimax(object):

    def __init__(self, heuristic_eval):

        self.heuristic_eval = heuristic_eval

    def minimax(self, board, parentBoard, depth, player, opponent,
                alfa=-INFINITY, beta=INFINITY):
        bestChild = board
        if depth == 0:
            return (self.heuristic_eval(parentBoard, board, depth,
                                        player, opponent), board)
        for child in board.next_states(player):
            score, newChild = self.minimax(
                child, board, depth - 1, opponent, player, -beta, -alfa)
            score = -score
            if score > alfa:
                alfa = score
                bestChild = child
            if beta <= alfa:
                break
        return (self.heuristic_eval(board, board, depth, player,
                                    opponent), bestChild)
