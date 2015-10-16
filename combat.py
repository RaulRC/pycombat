#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '== RPG COMBAT MODULE =='

NAME = 0
INITIATIVE = 1
HP = 2

class Player:
    def __init__(self, name='_player_', initiative=0, hp=0):
        self.name = name
        self.initiative = initiative
        self.hp = hp

    def show_player(self):
        return (self.name, self.initiative, self.hp)

    def hit_player(self, amount=0):
        self.hp += amount

    def change_initiative(self, initiative):
        self.initiative = initiative

class Combat:
    def __init__(self, players=[], rounds=0):
        self.players=players
        self.rounds=rounds

    def add_player(self, player):
        self.players.append(player)

    def add_players(self, players):
        self.players += players

    def next_round(self):
        self.rounds += 1



juanma = Player('Juanma',13,1)
print juanma.show_player()
juanma.hit_player(3)
print juanma.show_player()
