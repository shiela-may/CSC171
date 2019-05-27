
class State:

    def __init__(self, state, parent, move, depth, cost, key):

        self.state = state

        self.parent = parent

        self.move = move

        self.depth = depth

        self.cost = cost

        self.key = key

        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map

class State2:

    def __init__(self, state2, parent2, move2, depth2, cost2, key2):

        self.state2 = state2

        self.parent2 = parent2

        self.move2 = move2

        self.depth2 = depth2

        self.cost2 = cost2

        self.key2 = key2

        if self.state2:
            self.map2 = ''.join(str(e) for e in self.state2)

    def __eq__(self, other):
        return self.map2 == other.map2

    def __lt__(self, other):
        return self.map2 < other.map2
