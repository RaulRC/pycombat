#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ':: RPG COMBAT MODULE v0.1 LOADED ::'

NAME = 0
INITIATIVE = 1
HP = 2
INFINITE = 9999

OPTIONS = "---------------\n1.Add player\n2.Hit player\n3.Move player initiative\n4.Sort player's list\n5.Next round\n\n0.Exit\n---------------\n"

class Player:
    def __init__(self, name='_player_', initiative=0, hp=0):
        self.name = name
        self.initiative = initiative
        self.hp = hp

    def set_hp(self, hp=0):
        self.hp = hp

    def set_initiative(self, initiative=-1):
        self.initiative = initiative

    def set_name(self, name=''):
        self.name = name

    def show(self):
        return (self.name, self.initiative, self.hp)

    def hit_player(self, amount=0):
        self.hp += amount


class Combat:
    def __init__(self, players=[], rounds=1):
        self.players=players
        self.rounds=rounds

    def add_player(self, player):
        self.players.append(player)

    def add_players(self, players):
        self.players += players

    def next_round(self):
        self.rounds += 1

    def show_game(self):
        print 'Players: ' + str(map(lambda x: x.show(), self.players)) + '\nRound: ' + str(self.rounds)
    
    def show_indexed_list(self):
        result = ''
        for i in range(len(self.players)):
            result += ('[' + str(i) + ']' + str(self.players[i].show()) + '\n')
        print result

    def game_move_player(self):
        self.show_indexed_list()
        player_index = int(raw_input('Which player?: '))
        player_destiny = int(raw_input('To which position? '))
        self.players.insert(player_destiny, self.players.pop(player_index))

    def game_add_new_player(self):
        name = str(raw_input('Name: '))
        initiative = int(raw_input('Initiative: '))
        hp = int(raw_input('Hit points: '))
        p = Player(name, initiative, hp)
        self.add_player(p)
        self.show_game()

    def game_hit_player(self):
        self.show_indexed_list()
        player_index = int(raw_input('Which player?: '))
        hit_points = int(raw_input('How many points? '))
        self.players[player_index].hit_player(hit_points)
    
    def game_sort_players(self):
        self.players.sort(key=lambda x: x.initiative, reverse=True)

    def start(self):
        option = INFINITE
        player_index = 0
        hit_points = 0

        while option > 0:
            self.show_game()
            print OPTIONS
            try:
                option=int(raw_input('Select: '))
            except ValueError:
                print 'Try again'
            try:
                #ADD NEW PLAYER
                if option == 1:
                    self.game_add_new_player()
                #HIT PLAYER
                if option == 2: 
                    self.game_hit_player()
                #MOVE PLAYER
                if option == 3:
                    self.game_move_player()
                #SORT PLAYER's LIST
                if option == 4:
                    self.game_sort_players()
                #INCREMENT ROUND
                if option == 5:
                    self.next_round()
                if option == 0:
                    self.show_game()
                    print 'Combat finished!'
            except:
                print 'Try again, somethin happened!'
