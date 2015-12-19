import pprint


def parse_line(line):
    parts = line.split()
    if len(parts) == 3:
        return (parts[0], parts[2])

    if len(parts) == 0:
        return None

    if len(parts) == 1:
        return parts[0]

replacements = []
with open('else_input', 'r') as f:
    for line in f:
        if line.endswith('\n'):
            line = line[:-1]

        parsed = parse_line(line)
        if parsed is None:
            continue

        if isinstance(parsed, tuple):
            replacements.append(parsed)

        if isinstance(parsed, str):
            medicine = parsed

# Now start an a* search (sort of)

def score(node):
    return len(node[0]) + node[1]

open_nodes = set()
open_nodes.add((medicine, 0))
closed_nodes = set()


def replacement_options(X):
    """Get the result of every replacement option."""
    for i, j in replacements:
        for k in range(len(X)):
            if X[k:k+len(j)] == j:
                y = X[:k] + i + X[k + len(j):]
                yield y

while len(open_nodes) > 0:
    # open the node
    node = sorted(open_nodes, key=score)[0]
    if node[0] == 'e':
        print 'HALLELUJAH'
        break

    open_nodes.remove(node)
    closed_nodes.add(node[0])

    print len(closed_nodes), score(node), node[1], node[0]

    # For speed, only take the top couple of choices
    a = 0
    for option in replacement_options(node[0]):
        if a > 1:
            break
        a += 1
        if option in closed_nodes:
            continue

        open_nodes.add((option, node[1] + 1))

print node
