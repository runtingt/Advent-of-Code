import collections

# This is my first experience with a graph problem, so I use a bit of help from a tutorial
test_input_1 = '''\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

test_input_2 = '''\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''

# Import data
file = open("day12.txt", "r")
data = file.read()
file.close()

# The input are the edges of a bidirectional graph
# We can ony visit lower-case nodes once and upper case nodes as many times as we like

### Part One ###
# We are asked to count the number of possible paths from the start to the end
def get_all_paths_p1(string):
    edges = collections.defaultdict(set) # Create a dictionary where the values are sets
    for line in string.splitlines():
        source, destination = line.split('-')
        # Bidirectional so add source to destination and vice versa
        edges[source].add(destination)
        edges[destination].add(source)
        
    # Depth first seach
    # List of paths
    to_search = [('start',)] # Use a deque if we want breadth-first, then use popleft
    # Note in the above line, the comma makes pop() return the tuple ('start') not a str
    all_paths = set()
    while to_search:
        # Get the path to search
        path = to_search.pop()
        
        # Check if we have reached the end
        if path[-1] == 'end':
            all_paths.add(path)
            continue # Skip the iterations below
        
        # Get all the nodes we can go to from the last (most recent) element in the path
        for candidate in edges[path[-1]]:
            # Add to the path if it's upper-case or it's not in the path already
            if not candidate.islower() or candidate not in path:
                to_search.append((*path, candidate))
    
    return all_paths
    
all_paths = get_all_paths_p1(data)
print("Total paths: {0}".format(len(all_paths)))

#### Part Two ####
# Now we are allowed to visit a *single* lower case node twice
# We can't revisit start (not a problem before as it was lowercase)
# When we reach the end we immediately end
def get_all_paths_p2(string):
    edges = collections.defaultdict(set) # Create a dictionary where the values are sets
    for line in string.splitlines():
        source, destination = line.split('-')
        # Bidirectional so add source to destination and vice versa
        edges[source].add(destination)
        edges[destination].add(source)
        
    # Depth first seach
    # List of paths
    to_search = [(('start',), False)] # Flag to check if we've double-visited a small cave
    all_paths = set()
    while to_search:
        # Get the path to search
        path, double_cave = to_search.pop()
        
        # Check if we have reached the end
        if path[-1] == 'end':
            all_paths.add(path)
            continue # Skip the iterations below
        
        # Get all the nodes we can go to from the last (most recent) element in the path
        for candidate in edges[path[-1]]:
            # Ensure we don't revisit start
            if candidate == 'start':
                continue
            # Allow us to visit if upper case or not in path
            elif candidate.isupper() or candidate not in path:
                to_search.append(((*path, candidate), double_cave))
            # Allow us to visit if we haven't double visited a cave yet
            elif not double_cave:
                to_search.append(((*path, candidate), True))
                
    return all_paths

all_paths = get_all_paths_p2(data)
print("Total paths: {0}".format(len(all_paths)))
