from random import shuffle


def parse_line(line):
    parts = line.split()
    if len(parts) == 3:
        return (parts[0], parts[2])

    if len(parts) == 0:
        return None

    if len(parts) == 1:
        return parts[0]

reps = []
with open('input', 'r') as f:
    for line in f:
        parsed = parse_line(line)
        if parsed is None:
            continue
        if isinstance(parsed, tuple):
            reps.append(parsed)
        if isinstance(parsed, str):
            medicine = parsed

target = medicine
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    print tmp, target, len(tmp), len(target)
    if tmp == target:
        target = medicine
        part2 = 0
        shuffle(reps)

print part2
