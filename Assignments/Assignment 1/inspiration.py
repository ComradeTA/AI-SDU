class Node:
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.HEURISTICS = HEURISTICS[self.STATE]
        self.TRAVEL_COST = 0
        self.TOTAL_HEURISTICS = 0

    def path(self):
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:
            current_node = current_node.PARENT_NODE 
            path.append(current_node)
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return f'State: {str(self.STATE)} - Depth: {str(self.DEPTH)} - Heuristics: {str(self.HEURISTICS)} - Travel cost: {str(self.TRAVEL_COST)} - Total heuristics: {str(self.TOTAL_HEURISTICS)}'


def A_STAR_SEARCH():
    fringe_open = []
    fringe_closed = []

    initial_node = Node(INITIAL_STATE)
    initial_node.TOTAL_HEURISTICS = initial_node.TRAVEL_COST + initial_node.HEURISTICS

    fringe_open = INSERT(initial_node, fringe_open)

    while fringe_open is not None:
        current_node = fringe_open[0]
        current_index = 0

        for index, node in enumerate(fringe_open):
            if node.TOTAL_HEURISTICS < current_node.TOTAL_HEURISTICS:
                current_node = node
                current_index = index

        fringe_open.pop(current_index)
        fringe_closed.append(current_node)

        if current_node.STATE in GOAL_STATES:
            return current_node.path()

        children = EXPAND(current_node)
        for child in children:
            for closed_child in fringe_closed:
                if child == closed_child:
                    continue
            for open_node in fringe_open:
                if child == open_node and child.g > open_node.g:
                    continue
            fringe_open.append(child)

'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(child)
        s.STATE = child
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        s.TRAVEL_COST = node.TRAVEL_COST + COST_PATH[(node.STATE, child)]
        s.TOTAL_HEURISTICS = s.TRAVEL_COST + s.HEURISTICS
        successors = INSERT(s, successors)
    return successors

'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)
    return queue

'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    return queue.pop(0)

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):
    return STATE_SPACE[state]

'''
Environment Data, Goal States, Initial State, Heuristics, Cost between states
'''
INITIAL_STATE = ('A', 'Dirty', 'Dirty')
GOAL_STATES = [('A', 'Clean', 'Clean'), ('B', 'Clean', 'Clean')]

STATE_SPACE = {
    ('A', 'Dirty', 'Dirty'): [('A', 'Clean', 'Dirty'), ('B', 'Dirty', 'Dirty')],
    ('A', 'Clean', 'Dirty'): [('A', 'Clean', 'Clean')],
    ('A', 'Dirty', 'Clean'): [('A', 'Clean', 'Clean')],
    ('B', 'Dirty', 'Dirty'): [('B', 'Clean', 'Dirty'), ('A', 'Dirty', 'Dirty')],
    ('B', 'Clean', 'Dirty'): [('B', 'Clean', 'Clean')],
    ('B', 'Dirty', 'Clean'): [('B', 'Clean', 'Clean')]
}

HEURISTICS = {
    ('A', 'Dirty', 'Dirty'): 1,
    ('A', 'Clean', 'Dirty'): 4,
    ('A', 'Dirty', 'Clean'): 4,
    ('B', 'Dirty', 'Dirty'): 2,
    ('B', 'Clean', 'Dirty'): 6,
    ('B', 'Dirty', 'Clean'): 6,
    ('A', 'Clean', 'Clean'): 2,
    ('B', 'Clean', 'Clean'): 2
}

COST_PATH = {
    (('A', 'Dirty', 'Dirty'), ('A', 'Clean', 'Dirty')): 4,
    (('A', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Dirty')): 3,
    (('A', 'Clean', 'Dirty'), ('A', 'Clean', 'Clean')): 5,
    (('A', 'Dirty', 'Clean'), ('A', 'Clean', 'Clean')): 5,
    (('B', 'Dirty', 'Dirty'), ('B', 'Clean', 'Dirty')): 3,
    (('B', 'Dirty', 'Dirty'), ('A', 'Dirty', 'Dirty')): 0,
    (('B', 'Clean', 'Dirty'), ('B', 'Clean', 'Clean')): 4,
    (('B', 'Dirty', 'Clean'), ('B', 'Clean', 'Clean')): 4
}

'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = A_STAR_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()

if __name__ == '__main__':
    run()
