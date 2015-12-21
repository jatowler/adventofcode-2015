#!/usr/bin/env python
'''Solve AoC 2015 Day 21 Parts 1 and 2'''

def damage(attacker, defender):
    '''Calculate how much damage an attacker does in one turn.

    Total damage is the attacker's damage minus the defender's armor,
    except the attacker always does at least one damage.
    '''
    return max(1, attacker['damage'] - defender['armor'])

def fight(player, boss):
    '''Simulate a complete fight between the player and the boss.

    The player always goes first.

    The first combatant to have zero or fewer hit points loses.

    Returns True if player wins; False if boss wins
    '''
    while True:
        boss['hit'] -= damage(player, boss)

        if boss['hit'] <= 0:
            # player wins
            return True

        player['hit'] -= damage(boss, player)

        if player['hit'] <= 0:
            # boss wins
            return False

def generate_player(weapon, armor, ring1, ring2):
    '''Generate a new player with the given buffs.'''

    # Start with a standard-normal player
    player = {'hit': 100, 'damage': 0, 'armor': 0}

    # Apply buffs
    player['damage'] = (w['damage'] +
                        ring1['damage'] +
                        ring2['damage'])

    player['armor'] = (a['armor'] +
                       ring1['armor'] +
                       ring2['armor'])

    return player

def generate_boss():
    '''Generate a new standard-normal boss.'''
    return {'hit': 109, 'damage': 8, 'armor': 2}

def weapon(name, cost, damage):
    '''Convenience function to create a weapon.'''
    return {'name': name, 'cost': cost, 'damage': damage}

def armor(name, cost, armor):
    '''Convenience function to create an armor.'''
    return {'name': name, 'cost': cost, 'armor': armor}

def ring(name, cost, damage, armor):
    ''' Convenience function to create a ring.'''
    return {'name': name, 'cost': cost, 'damage': damage, 'armor': armor}


# We must choose exactly one weapon
weapons = [weapon('dagger', 8, 4),
           weapon('shortsword', 10, 5),
           weapon('warhammer', 25, 6),
           weapon('longsword', 40, 7),
           weapon('greataxe', 74, 8)]

# We may choose zero or one armors, so add a useless armor to stand in for
# no armor
armor = [armor('none', 0, 0),
         armor('leather', 13, 1),
         armor('chainmail', 31, 2),
         armor('splintmail', 53, 3),
         armor('bandedmail', 75, 4),
         armor('platemail', 102, 5)]

# We may choose zero, one, or two rings, so add two useless rings to stand
# in for no rings
rings = [ring('none', 0, 0, 0),
         ring('none', 0, 0, 0),
         ring('damage +1', 25, 1, 0),
         ring('damage +2', 50, 2, 0),
         ring('damage +3', 100, 3, 0),
         ring('defense +1', 20, 0, 1),
         ring('defense +2', 40, 0, 2),
         ring('defense +3', 80, 0, 3)]


# Run through every combination of weapon, armor, and rings and simulate
# a battle. Catalog the results.
results = []
for w in weapons:
    for a in armor:
        for i in xrange(len(rings)):
            ring1 = rings[i]
            for j in xrange(i + 1, len(rings)):
                ring2 = rings[j]

                cost = (w['cost'] +
                        a['cost'] +
                        ring1['cost'] +
                        ring2['cost'])

                player = generate_player(w, a, ring1, ring2)
                boss = generate_boss()
                result = (cost,
                          fight(player, boss),
                          player,
                          w['name'],
                          a['name'],
                          ring1['name'],
                          ring2['name'])
                results.append(result)

cheapest_victory = sorted(r for r in results if r[1] == True)[0]
costliest_loss = sorted(r for r in results if r[1] == False)[-1]

print 'Cheapest victory: {}'.format(cheapest_victory)
print 'Costliest loss: {}'.format(costliest_loss)

import pprint
pprint.pprint([(r[0], r[1], r[2]) for r in results])
