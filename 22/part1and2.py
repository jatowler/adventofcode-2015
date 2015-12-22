#!/usr/bin/env python
"""Solve AoC 2015, Day 22 Parts 1 and 2"""

import pprint

PRINT = False

def damage(attacker, defender):
    '''Calculate how much damage an attacker does in one turn.

    Total damage is the attacker's damage minus the defender's armor,
    except the attacker always does at least one damage.
    '''
    return max(1, attacker['damage'] - defender['armor'])

def apply_effects(player, boss):
    for i, effect in enumerate(player['effects']):
        if effect[0] == 'shield':
            player['armor'] = 7
            if PRINT:
                print 'Applied shield, increasing player\'s armor to 7'
        elif effect[0] == 'poison':
            boss['hit'] -= 3
            if PRINT:
                print 'Boss takes 3 damage from poison'
        elif effect[0] == 'recharge':
            player['mana'] += 101
            if PRINT:
                print 'Player gains 101 mana from recharge'

        turns_left = effect[1] - 1
        player['effects'][i] = (effect[0], turns_left)

        if PRINT:
            print '  "{}" has {} turns left'.format(effect[0], turns_left)

    # Delete all effects that have been worn out
    for effect in player['effects']:
        if effect[1] <= 0:
            # Remove effect
            if PRINT:
                print '  "{}" has ended.'.format(effect[0])
            player['effects'].remove(effect)

def turn(player, boss, spell, hard_mode=False):
    if PRINT:
        print ''
        print '---PLAYER TURN---'
        print 'Player has {} hp, {} mana, {} armor'.format(player['hit'],
                                                           player['mana'],
                                                           player['armor'])
        print 'Boss has {} hp'.format(boss['hit'])

    # player turn
    if hard_mode == True:
        player['hit'] -= 1

    # negate effects
    player['armor'] = 0
    apply_effects(player, boss)

    if player['hit'] <= 0:
        if PRINT:
            print 'Boss wins'
        return (True, 'boss')
    if boss['hit'] <= 0:
        if PRINT:
            print 'Player wins'
        return (True, 'player')

    # Apply spells
    if spell == 'magic_missile':
        player['mana'] -= 53
        boss['hit'] -= 4
    elif spell == 'drain':
        player['mana'] -= 73
        boss['hit'] -= 2
        player['hit'] += 2
    elif spell == 'shield':
        player['mana'] -= 113
        player['effects'].append(('shield', 6))
    elif spell == 'poison':
        player['mana'] -= 173
        player['effects'].append(('poison', 6))
    elif spell == 'recharge':
        player['mana'] -= 229
        player['effects'].append(('recharge', 5))

    if PRINT:
        print 'Player casts "{}"'.format(spell)

    if player['mana'] < 0:
        if PRINT:
            print 'OOM; Boss wins'
        return (True, 'boss')
    if player['hit'] <= 0:
        if PRINT:
            print 'Boss wins'
        return (True, 'boss')
    if boss['hit'] <= 0:
        if PRINT:
            print 'Player wins'
        return (True, 'player')

    # boss turn
    if PRINT:
        print '---BOSS TURN---'
        print 'Player has {} hp, {} mana, {} armor'.format(player['hit'],
                                                           player['mana'],
                                                           player['armor'])
        print 'Boss has {} hp'.format(boss['hit'])

    # reset effects
    player['armor'] = 0
    apply_effects(player, boss)

    if player['hit'] <= 0:
        if PRINT:
            print 'Boss wins'
        return (True, 'boss')
    if boss['hit'] <= 0:
        if PRINT:
            print 'Player wins'
        return (True, 'player')

    boss_damage = damage(boss, player)
    player['hit'] -= boss_damage

    if PRINT:
        print 'Boss attacks for {} damage'.format(boss_damage)

    if player['hit'] <= 0:
        if PRINT:
            print 'Boss wins'
        return (True, 'boss')
    if boss['hit'] <= 0:
        if PRINT:
            print 'Player wins'
        return (True, 'player')

    return (False, 'nobody')

def new_boss():
    """Generate a standard-normal boss."""
    return {'hit': 55, 'damage': 8}

def new_player():
    """Generate a standard-normal player."""
    return {'hit': 50, 'mana': 500, 'armor': 0, 'effects': []}

def spell(name, cost, turns):
    """Convenience method for creating a spell.

    Instants have turns = 0.
    
    The player's move and the boss's move both count as turns.
    """
    return {'name': name, 'cost': cost, 'turns': turns}

spells = [spell('magic_missile',  53, 0), 
          spell('drain',          73, 0),
          spell('shield',        113, 6),
          spell('poison',        173, 6),
          spell('recharge',      229, 5)]

# Let's try randomly casting spells
import random
results = []
min_mana = 1e9
while True:
    if PRINT:
        print ''
        print ''
        print '============'
        print '= NEW GAME ='
        print '============'
        print ''

    boss = new_boss()
    player = new_player()
    mana_cost = 0
    game_over = False

    while game_over == False:
        spell = random.choice(spells)
        mana_cost += spell['cost']

        if mana_cost > 2134:
            game_over = True
            continue
        
        effects = [e[0] for e in player['effects'] if e[1] > 1]
        if spell['name'] in effects:
            game_over = True

        result = turn(player, boss, spell['name'])
        if result[0] == True:
            results.append((result[1], mana_cost))
            if result[1] == 'player':
                if mana_cost < min_mana:
                    min_mana = mana_cost
                print 'Player wins! (cost: {}; min: {})'.format(mana_cost,
                                                                min_mana)

            game_over = True
