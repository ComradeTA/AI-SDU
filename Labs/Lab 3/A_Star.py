class Node: # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth
        self.HEURISTICS = HEURISTICS[self.STATE]
        self.PATH_COST = 0
        self.ESTIMATED_COST = 0

    def path(self): # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE: # while current node has parent
            current_node = current_node.PARENT_NODE # make parent the current node
            path.append(current_node) # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH) + ' - Heuristics: ' + str(self.HEURISTICS) + ' - Path cost: ' + str(self.PATH_COST) + ' - Estimated cost: ' + str(self.ESTIMATED_COST)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def A_STAR_SEARCH():
    fringe = []
    closed_paths = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = GET_BEST_HEURISTIC_NODE(fringe, closed_paths)
        for GOAL_STATE in GOAL_STATES:
            if node.STATE == GOAL_STATE:
                return node.path()
        
        # Remove dead end paths
        if len(successor_fn(node.STATE)) == 0:
            CLOSE_PATH(node, closed_paths)
            continue
            
        
        children = EXPAND(node)
        fringe = REMOVE(node, fringe)
        fringe = INSERT_ALL(children, fringe)
        print("Fringe: {}".format(fringe))
        print("*******")
    print("GOAL NOT FOUND")


def GET_BEST_HEURISTIC_NODE(node_list, node_blacklist = []):
    node_list = [x for x in node_list if x not in node_blacklist]
    best_node = node_list[0]
    for node in node_list:
        if best_node.ESTIMATED_COST > node.ESTIMATED_COST:
            best_node = node
    return best_node

def CLOSE_PATH(node, closed_paths):
    potential_paths = [x for x in successor_fn(node.STATE) if x not in closed_paths]

    if len(potential_paths) == 0:
        closed_paths.append(node)
        closed_paths = CLOSE_PATH(node.PARENT_NODE, closed_paths)
    
    return closed_paths



'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(child) # create node for each in state list
        s.STATE = child # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        s.PATH_COST = node.PATH_COST + COST_PATHS[node.STATE][STATE_SPACE[node.STATE].index(child)]
        s.ESTIMATED_COST = s.PATH_COST + s.HEURISTICS
        successors = INSERT(s, successors)
    return successors

'''
Insert node in to the queue (fringe)
'''
def INSERT(node, queue):
    queue.append(node)
    return queue


'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for l in list:
        queue.append(l)
    return queue    
 

'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    return queue.pop(0)

def REMOVE(node, queue):
    queue.remove(node)
    return queue



'''
Successor function,mapping the nodes to its successors
'''
def successor_fn(state): # Lookup list of successor states
    return STATE_SPACE[state] # successor_fn( 'c' ) returns ['F', 'G']



INITIAL_STATE = 'A'
GOAL_STATES = ['K', 'L']
STATE_SPACE = { 'A': ['B', 'C', 'D'],
                'B': ['F', 'E'], 'C': ['E'], 'D': ['H', 'I', 'J'],
                'E': ['G', 'H'], 'F': ['G'], 'G': ['K'],
                'H': ['K', 'L'], 'I': ['L'], 'J': [], 'K': [], 'L': []}
HEURISTICS = { 'A': 6,
               'B': 5, 'C': 5, 'D': 2,
               'E': 4, 'F': 5, 'G': 4,
               'H': 1, 'I': 2,  'J': 1, 'K': 0, 'L': 0}
COST_PATHS = { 'A': [1, 2, 4],
                'B': [5, 4], 'C': [1], 'D': [1, 4, 2],
                'E': [2, 3], 'F': [1], 'G': [6],
                'H': [6, 5], 'I': [3], 'J': [], 'K': [], 'L': []}
'''
Run tree seach and display the nodes in the path to goal node
'''
def run():
    path = A_STAR_SEARCH()
    print('Solution path: ')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()