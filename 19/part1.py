import re

def parse_line(line):
    parts = line.split()
    if len(parts) == 3:
        return (parts[0], parts[2])

    if len(parts) == 0:
        return None

    if len(parts) == 1:
        return parts[0]

replacements = []
start = ''
with open('input', 'r') as f:
    for line in f:
        parsed = parse_line(line)
        if parsed is None:
            continue
        if isinstance(parsed, tuple):
            replacements.append(parsed)
        if isinstance(parsed, str):
            start = parsed

distinct = set()
for r in replacements:
    matches = [(match.start(), match.end()) for match in re.finditer(r[0], start)]
    for m in matches:
        distinct.add(start[:m[0]] + r[1] + start[m[1]:])

print len(distinct)
